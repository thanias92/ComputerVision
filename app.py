import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import time

# ======== Load model YOLOv8 dengan error handling =========
try:
    model = YOLO("bestyolo.pt")  # Ganti dengan nama model custom-mu
    print("✅ Model berhasil dimuat!")
    print(f"📦 Classes yang tersedia: {model.names}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

# ======== Fungsi Deteksi Gambar =========
def detect_image(image):
    try:
        if image is None:
            return None, "Tidak ada gambar yang diupload"

        img_array = np.array(image)
        
        # Gunakan confidence threshold secara eksplisit
        results = model.predict(img_array, conf=0.25)[0]
        print("🔍 Jumlah Boxes:", len(results.boxes) if results.boxes is not None else "Tidak ada")

        # Visualisasi hasil
        annotated = results.plot()
        annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        detections = 0
        summary = "Tidak ada objek yang terdeteksi"

        if hasattr(results, 'boxes') and results.boxes is not None and len(results.boxes) > 0:
            detections = len(results.boxes)
            summary = f"Terdeteksi {detections} objek"
            try:
                classes = results.boxes.cls.cpu().numpy()
                class_names = []
                for cls in classes:
                    cls_int = int(cls)
                    if cls_int in model.names:
                        class_names.append(model.names[cls_int])
                    else:
                        class_names.append(f"Unknown_{cls_int}")
                class_counts = {}
                for name in class_names:
                    class_counts[name] = class_counts.get(name, 0) + 1
                if class_counts:
                    summary += "\nDetail:\n"
                    for class_name, count in class_counts.items():
                        summary += f"- {class_name}: {count}\n"
            except Exception as e:
                summary += f"\n(Error dalam detail klasifikasi: {str(e)})"
        return annotated_rgb, summary

    except Exception as e:
        return None, f"Error dalam deteksi gambar: {str(e)}"

# ======== Fungsi Deteksi dari Webcam Frame ========
def detect_from_webcam_frame(image):
    if image is not None:
        return detect_image(Image.fromarray(image))
    return None, "Tidak ada frame yang tersedia"

# ======== CSS Custom untuk Tampilan ========
css = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
h1 {
    text-align: center;
    color: #2E8B57;
    margin-bottom: 30px;
}
"""

# ======== Gradio UI App ========
with gr.Blocks(css=css, title="Motorcycle Detector") as app:
    gr.Markdown("# 🏍️ Deteksi Sepeda Motor Menggunakan Kamera & Gambar")

    with gr.Tabs():
        # Tab Upload Gambar
        with gr.TabItem("📷 Upload Gambar"):
            gr.Markdown("### Upload gambar untuk mendeteksi sepeda motor")
            with gr.Row():
                with gr.Column():
                    image_input = gr.Image(type="pil", label="Upload Gambar")
                    detect_btn = gr.Button("🔍 Deteksi Objek", variant="primary")
                with gr.Column():
                    image_output = gr.Image(label="Hasil Deteksi")
                    summary_output = gr.Textbox(label="Ringkasan Deteksi", lines=5)
            detect_btn.click(fn=detect_image, inputs=image_input, outputs=[image_output, summary_output])

        # Tab Manual Webcam (Laptop Only)
        with gr.TabItem("📸 Manual Webcam"):
            gr.Markdown("### Gunakan kamera Anda untuk deteksi sepeda motor")

            with gr.Row():
                with gr.Column():
                    webcam_input_manual = gr.Image(source="webcam", streaming=True, label="Kamera Laptop (Webcam)")
                    detect_webcam_btn = gr.Button("📸 Ambil & Deteksi", variant="primary")
                with gr.Column():
                    webcam_result_img = gr.Image(label="Hasil Deteksi")
                    webcam_result_text = gr.Textbox(label="Ringkasan Deteksi", lines=5)

            detect_webcam_btn.click(
                fn=detect_from_webcam_frame,
                inputs=webcam_input_manual,
                outputs=[webcam_result_img, webcam_result_text]
            )

    # Footer
    gr.Markdown("""
    ---
    ### 🔧 Informasi Teknis
    - Model: YOLOv8 Custom (bestyolo.pt)
    - Objek yang dapat dideteksi: Sepeda Motor
    - Format gambar: JPG, PNG, WEBP

    ### 📸 Cara Menggunakan:
    - Upload gambar ke tab pertama
    - Atau gunakan kamera laptop di tab "Manual Webcam" dan klik tombol "Ambil & Deteksi"

    ### ⚡ Tips:
    - Gunakan pencahayaan yang cukup
    - Pastikan kamera mengarah jelas ke objek sepeda motor
    - Gunakan browser laptop (Chrome/Edge) agar webcam terdeteksi dengan baik
    """)
    
# ======== Jalankan App ========
if __name__ == '__main__':
    app.launch(share=True, debug=True, inbrowser=False)