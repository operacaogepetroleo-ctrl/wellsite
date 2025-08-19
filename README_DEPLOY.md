
# Deploy do Wellsite (backend Flask + frontend)

Gerado em 2025-08-19

## Rota recomendada
- Backend no **Render** (Plano Free/Starter)
- Frontend no **Vercel** (ou Render Static Site)

### Passo a passo resumido
1) Suba seu repo no GitHub com esta estrura:
   ```
   wellsite/
     backend/...
     frontend/...
     render.yaml
   ```
2) Render:
   - New > Web Service > selecione seu repo.
   - Ele vai ler `render.yaml` e criar o serviço backend.
   - Configure env vars: OPENAI_API_KEY (Secret), OPENAI_MODEL, etc.
   - O serviço cria um disco `/var/data` para uploads e logs.
3) Frontend:
   - Se for só arquivos estáticos (ex.: ai_demo.html), use **Vercel** com `vercel.json`.
   - Se for React/Vite, use o bloco comentado no `render.yaml` e build para `frontend/dist`.
4) Atualize `CORS_ORIGINS` com o domínio real do frontend.
5) Teste:
   - `GET https://<backend-domain>/api/health`
   - `POST https://<backend-domain>/api/ai/extract_v2` (enviando PDF)
