from fastapi import APIRouter
from app.services import spaceship_service
from app.api.schemas.contract import ContractList
from app.api.mappers.spaceship_mappers import toResponse, toContracts

router = APIRouter(
    prefix="/spaceship"
)

@router.post("/optimize")
async def optimize(contractList: ContractList):
    result = spaceship_service.optimize(toContracts(contractList))
    return toResponse(result)

@router.post("/brute-force")
async def brute_force(contractList: ContractList):
    result = spaceship_service.brute_force(toContracts(contractList))
    return toResponse(result)

@router.post("/first-come-first-served")
async def fcfs(contractList: ContractList):
    result = spaceship_service.fcfs(toContracts(contractList))
    return toResponse(result)

@router.post("/greedy-selection")
async def greedy_selection(contractList: ContractList):
    result = spaceship_service.greedy_selection(toContracts(contractList))
    return toResponse(result)

@router.post("/random-selection")
async def random_selection(contractList: ContractList):
    result = spaceship_service.random_selection(toContracts(contractList))
    return toResponse(result)