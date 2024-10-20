-- columns 'band_name' and 'lifespan' (years until 2022)
-- use attributes formed and split for computing 'lifespan'
SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE style='Glam rock';
