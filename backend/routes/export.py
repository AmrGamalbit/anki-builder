from fastapi import APIRouter, BackgroundTasks
from services.generator import DeckGenerator
from models.requests import ExportRequest

router = APIRouter(prefix="/deck", tags=["deck"])


@router.post("/export")
async def export(request: ExportRequest, background_tasks: BackgroundTasks):
    generator = DeckGenerator(
        definition_options=request.definition_options,
        appearance_options=request.appearance_options,
        deck_name=request.deck_name,
        tags=request.tags,
    )
    return await generator.export_deck(
        entries=request.data,
        background_tasks=background_tasks,
    )
