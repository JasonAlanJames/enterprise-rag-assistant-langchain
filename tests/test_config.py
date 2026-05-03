from app.config import settings


def test_default_model_name_exists():
    assert settings.model_name is not None
    assert isinstance(settings.model_name, str)
    assert len(settings.model_name) > 0


def test_embedding_model_exists():
    assert settings.embedding_model is not None
    assert isinstance(settings.embedding_model, str)
    assert len(settings.embedding_model) > 0


def test_vector_db_path_exists_as_setting():
    assert settings.vector_db_path is not None


def test_documents_path_exists_as_setting():
    assert settings.documents_path is not None