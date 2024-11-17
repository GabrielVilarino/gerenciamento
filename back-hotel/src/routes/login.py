from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import LoginRequest
from pool.pool import get_db
from pool.models import Usuario

router = APIRouter()

@router.post("/login")
async def login(user: LoginRequest, db: AsyncSession = Depends(get_db)):
    """
    Rota para autenticação de usuário pelo usuário e senha.
    """
    try:
        # Realiza a consulta
        query = select(Usuario).where(
            Usuario.usuario == user.usuario,
            Usuario.senha == user.senha
        )
        result = await db.execute(query)
        usuario = result.fetchone()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário ou Senha incorretos.")
        
        usuario_data = usuario[0]

        return {
            "detail": "sucesso",
            "id": usuario_data.id,
            "usuario": usuario_data.usuario,
            "senha": usuario_data.senha
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao buscar o usuário")
