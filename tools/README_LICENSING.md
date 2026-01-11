# tablint Offline License Generation (Pro)

## WARNING
- **NEVER commit your private key to git or share it.**
- Store your private key securely, outside the repository.
- Only the public key (if needed) should be embedded in the app.

## Key Generation (Demo: Simple Secret)
- For this demo, the "private key" is just a secret string in a text file (private_key.txt).
- In production, use a real asymmetric keypair (e.g., RSA) and update the verifier/generator accordingly.

### Steps:
1. **Create a private key file:**
   - Generate a random string and save it as `private_key.txt` (outside the repo).
   - Example: `openssl rand -hex 32 > private_key.txt`
2. **(Optional) Update public key in app:**
   - If using a real keypair, embed the public key in `tablint/license.py`.
   - For this demo, the public key is not used (signature is just sha256 hash).
3. **Generate a license:**
   - Run the generator script:
     ```
     python tools/generate_license.py --email user@example.com --name "User Name" --private-key /path/to/private_key.txt --output license.json
     ```
   - The output file (e.g., `license.json`) contains the signed license.
4. **Deliver the license:**
   - Send the license file to the user (e.g., via Gumroad delivery).
   - User should place it as `~/.csv_guard.license` or `./csv_guard.license`.

## File/Key Management
- **private_key.txt**: Store securely, never commit.
- **public_key.pem**: Only needed if using real asymmetric crypto.
- **license files**: Do not commit generated licenses to the repo.

## Updating the Public Key
- If you change the keypair, update the embedded public key in `tablint/license.py`.
- All new licenses must be signed with the new private key.

## License Format
- JSON with two fields:
  - `payload`: JSON string with `email`, `name`, `tier` (must be 'pro')
  - `signature`: sha256 hash of payload (for demo; use real signature in production)

## Example License File
```
{
  "payload": "{\"email\":\"user@example.com\",\"name\":\"User Name\",\"tier\":\"pro\"}",
  "signature": "...sha256..."
}
```
