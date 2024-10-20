-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- script can be executed on any database
SELECT origin, fans AS nb_fans
FROM metal_bands
ORDER BY nb_fans DESC;
