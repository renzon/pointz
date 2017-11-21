def sql_transaction_to_bigquery_row(transaction):
    return (
        transaction.id,
        int(100 * transaction.sale),
        int(100 * transaction.pointz_sale),
        transaction.pointz,
        transaction.creation.year,
        transaction.creation.month,
        transaction.creation.day,
        transaction.subsidiary.name,
        transaction.subsidiary.id,
        transaction.subsidiary.region.name,
        transaction.subsidiary.region.id,
        transaction.subsidiary.region.partner.name,
        transaction.subsidiary.region.partner.id,
        transaction.subsidiary.region.partner.segment
    )
