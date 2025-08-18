from fastapi import FastAPI, APIRouter, Depends
from fastapi.responses import StreamingResponse
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from auth.dependencies import get_authenticated_agent_db
from io import BytesIO

app = FastAPI()

router = APIRouter(
    tags=['download']
    )


@router.post("/download-pdf")
async def generate_biodata_pdf(user_data: dict, user_db=Depends(get_authenticated_agent_db)):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Styles
    styles = getSampleStyleSheet()
    heading_style = ParagraphStyle(
        name="Heading",
        fontSize=18,
        alignment=1,  # Center
        spaceAfter=20,
        fontName="Helvetica-Bold"
    )
    normal_style = styles["Normal"]

    elements = []

    # Heading
    elements.append(Paragraph("SAGAI Matrimonial AI Tool", heading_style))
    elements.append(Spacer(1, 20))

    # User Details
    for key, value in user_data.items():
        elements.append(Paragraph(f"<b>{key.replace('_', ' ').title()}</b>: {value}", normal_style))
        elements.append(Spacer(1, 12))

    # Build PDF
    doc.build(elements)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename=sagai_matrimony.pdf"
    })
