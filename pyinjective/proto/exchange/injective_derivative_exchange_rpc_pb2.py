# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/injective_derivative_exchange_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0exchange/injective_derivative_exchange_rpc.proto\x12!injective_derivative_exchange_rpc\"<\n\x0eMarketsRequest\x12\x15\n\rmarket_status\x18\x01 \x01(\t\x12\x13\n\x0bquote_denom\x18\x02 \x01(\t\"[\n\x0fMarketsResponse\x12H\n\x07markets\x18\x01 \x03(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeMarketInfo\"\xff\x05\n\x14\x44\x65rivativeMarketInfo\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rmarket_status\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x13\n\x0boracle_base\x18\x04 \x01(\t\x12\x14\n\x0coracle_quote\x18\x05 \x01(\t\x12\x13\n\x0boracle_type\x18\x06 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x07 \x01(\r\x12\x1c\n\x14initial_margin_ratio\x18\x08 \x01(\t\x12 \n\x18maintenance_margin_ratio\x18\t \x01(\t\x12\x13\n\x0bquote_denom\x18\n \x01(\t\x12\x46\n\x10quote_token_meta\x18\x0b \x01(\x0b\x32,.injective_derivative_exchange_rpc.TokenMeta\x12\x16\n\x0emaker_fee_rate\x18\x0c \x01(\t\x12\x16\n\x0etaker_fee_rate\x18\r \x01(\t\x12\x1c\n\x14service_provider_fee\x18\x0e \x01(\t\x12\x14\n\x0cis_perpetual\x18\x0f \x01(\x08\x12\x1b\n\x13min_price_tick_size\x18\x10 \x01(\t\x12\x1e\n\x16min_quantity_tick_size\x18\x11 \x01(\t\x12U\n\x15perpetual_market_info\x18\x12 \x01(\x0b\x32\x36.injective_derivative_exchange_rpc.PerpetualMarketInfo\x12[\n\x18perpetual_market_funding\x18\x13 \x01(\x0b\x32\x39.injective_derivative_exchange_rpc.PerpetualMarketFunding\x12^\n\x1a\x65xpiry_futures_market_info\x18\x14 \x01(\x0b\x32:.injective_derivative_exchange_rpc.ExpiryFuturesMarketInfo\"n\n\tTokenMeta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\x12\x0c\n\x04logo\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x63imals\x18\x05 \x01(\x11\x12\x12\n\nupdated_at\x18\x06 \x01(\x12\"\x8e\x01\n\x13PerpetualMarketInfo\x12\x1f\n\x17hourly_funding_rate_cap\x18\x01 \x01(\t\x12\x1c\n\x14hourly_interest_rate\x18\x02 \x01(\t\x12\x1e\n\x16next_funding_timestamp\x18\x03 \x01(\x12\x12\x18\n\x10\x66unding_interval\x18\x04 \x01(\x12\"f\n\x16PerpetualMarketFunding\x12\x1a\n\x12\x63umulative_funding\x18\x01 \x01(\t\x12\x18\n\x10\x63umulative_price\x18\x02 \x01(\t\x12\x16\n\x0elast_timestamp\x18\x03 \x01(\x12\"Q\n\x17\x45xpiryFuturesMarketInfo\x12\x1c\n\x14\x65xpiration_timestamp\x18\x01 \x01(\x12\x12\x18\n\x10settlement_price\x18\x02 \x01(\t\"\"\n\rMarketRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"Y\n\x0eMarketResponse\x12G\n\x06market\x18\x01 \x01(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeMarketInfo\")\n\x13StreamMarketRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\x8a\x01\n\x14StreamMarketResponse\x12G\n\x06market\x18\x01 \x01(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeMarketInfo\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"f\n\x1b\x42inaryOptionsMarketsRequest\x12\x15\n\rmarket_status\x18\x01 \x01(\t\x12\x13\n\x0bquote_denom\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\"\xa6\x01\n\x1c\x42inaryOptionsMarketsResponse\x12K\n\x07markets\x18\x01 \x03(\x0b\x32:.injective_derivative_exchange_rpc.BinaryOptionsMarketInfo\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\xf3\x03\n\x17\x42inaryOptionsMarketInfo\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rmarket_status\x18\x02 \x01(\t\x12\x0e\n\x06ticker\x18\x03 \x01(\t\x12\x15\n\roracle_symbol\x18\x04 \x01(\t\x12\x17\n\x0foracle_provider\x18\x05 \x01(\t\x12\x13\n\x0boracle_type\x18\x06 \x01(\t\x12\x1b\n\x13oracle_scale_factor\x18\x07 \x01(\r\x12\x1c\n\x14\x65xpiration_timestamp\x18\x08 \x01(\x12\x12\x1c\n\x14settlement_timestamp\x18\t \x01(\x12\x12\x13\n\x0bquote_denom\x18\n \x01(\t\x12\x46\n\x10quote_token_meta\x18\x0b \x01(\x0b\x32,.injective_derivative_exchange_rpc.TokenMeta\x12\x16\n\x0emaker_fee_rate\x18\x0c \x01(\t\x12\x16\n\x0etaker_fee_rate\x18\r \x01(\t\x12\x1c\n\x14service_provider_fee\x18\x0e \x01(\t\x12\x1b\n\x13min_price_tick_size\x18\x0f \x01(\t\x12\x1e\n\x16min_quantity_tick_size\x18\x10 \x01(\t\x12\x18\n\x10settlement_price\x18\x11 \x01(\t\"N\n\x06Paging\x12\r\n\x05total\x18\x01 \x01(\x12\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x11\x12\n\n\x02to\x18\x03 \x01(\x11\x12\x1b\n\x13\x63ount_by_subaccount\x18\x04 \x01(\x12\"/\n\x1a\x42inaryOptionsMarketRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"i\n\x1b\x42inaryOptionsMarketResponse\x12J\n\x06market\x18\x01 \x01(\x0b\x32:.injective_derivative_exchange_rpc.BinaryOptionsMarketInfo\"%\n\x10OrderbookRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"c\n\x11OrderbookResponse\x12N\n\torderbook\x18\x01 \x01(\x0b\x32;.injective_derivative_exchange_rpc.DerivativeLimitOrderbook\"\xa8\x01\n\x18\x44\x65rivativeLimitOrderbook\x12;\n\x04\x62uys\x18\x01 \x03(\x0b\x32-.injective_derivative_exchange_rpc.PriceLevel\x12<\n\x05sells\x18\x02 \x03(\x0b\x32-.injective_derivative_exchange_rpc.PriceLevel\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"@\n\nPriceLevel\x12\r\n\x05price\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\'\n\x12OrderbookV2Request\x12\x11\n\tmarket_id\x18\x01 \x01(\t\"g\n\x13OrderbookV2Response\x12P\n\torderbook\x18\x01 \x01(\x0b\x32=.injective_derivative_exchange_rpc.DerivativeLimitOrderbookV2\"\xbc\x01\n\x1a\x44\x65rivativeLimitOrderbookV2\x12;\n\x04\x62uys\x18\x01 \x03(\x0b\x32-.injective_derivative_exchange_rpc.PriceLevel\x12<\n\x05sells\x18\x02 \x03(\x0b\x32-.injective_derivative_exchange_rpc.PriceLevel\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"\'\n\x11OrderbooksRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"k\n\x12OrderbooksResponse\x12U\n\norderbooks\x18\x01 \x03(\x0b\x32\x41.injective_derivative_exchange_rpc.SingleDerivativeLimitOrderbook\"\x83\x01\n\x1eSingleDerivativeLimitOrderbook\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12N\n\torderbook\x18\x02 \x01(\x0b\x32;.injective_derivative_exchange_rpc.DerivativeLimitOrderbook\")\n\x13OrderbooksV2Request\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"o\n\x14OrderbooksV2Response\x12W\n\norderbooks\x18\x01 \x03(\x0b\x32\x43.injective_derivative_exchange_rpc.SingleDerivativeLimitOrderbookV2\"\x87\x01\n SingleDerivativeLimitOrderbookV2\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12P\n\torderbook\x18\x02 \x01(\x0b\x32=.injective_derivative_exchange_rpc.DerivativeLimitOrderbookV2\",\n\x16StreamOrderbookRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\xa7\x01\n\x17StreamOrderbookResponse\x12N\n\torderbook\x18\x01 \x01(\x0b\x32;.injective_derivative_exchange_rpc.DerivativeLimitOrderbook\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x12\x11\n\tmarket_id\x18\x04 \x01(\t\".\n\x18StreamOrderbookV2Request\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\xab\x01\n\x19StreamOrderbookV2Response\x12P\n\torderbook\x18\x01 \x01(\x0b\x32=.injective_derivative_exchange_rpc.DerivativeLimitOrderbookV2\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x12\x11\n\tmarket_id\x18\x04 \x01(\t\"2\n\x1cStreamOrderbookUpdateRequest\x12\x12\n\nmarket_ids\x18\x01 \x03(\t\"\xb8\x01\n\x1dStreamOrderbookUpdateResponse\x12Y\n\x17orderbook_level_updates\x18\x01 \x01(\x0b\x32\x38.injective_derivative_exchange_rpc.OrderbookLevelUpdates\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x12\x11\n\tmarket_id\x18\x04 \x01(\t\"\xd7\x01\n\x15OrderbookLevelUpdates\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x10\n\x08sequence\x18\x02 \x01(\x04\x12\x41\n\x04\x62uys\x18\x03 \x03(\x0b\x32\x33.injective_derivative_exchange_rpc.PriceLevelUpdate\x12\x42\n\x05sells\x18\x04 \x03(\x0b\x32\x33.injective_derivative_exchange_rpc.PriceLevelUpdate\x12\x12\n\nupdated_at\x18\x05 \x01(\x12\"Y\n\x10PriceLevelUpdate\x12\r\n\x05price\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"\x8b\x02\n\rOrdersRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x15\n\rsubaccount_id\x18\x03 \x01(\t\x12\x0c\n\x04skip\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x11\x12\x12\n\nstart_time\x18\x06 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x12\x12\x12\n\nmarket_ids\x18\x08 \x03(\t\x12\x16\n\x0eis_conditional\x18\t \x01(\t\x12\x12\n\norder_type\x18\n \x01(\t\x12\x18\n\x10include_inactive\x18\x0b \x01(\x08\x12\x1f\n\x17subaccount_total_orders\x18\x0c \x01(\x08\"\x94\x01\n\x0eOrdersResponse\x12G\n\x06orders\x18\x01 \x03(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeLimitOrder\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\xba\x03\n\x14\x44\x65rivativeLimitOrder\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x16\n\x0eis_reduce_only\x18\x05 \x01(\x08\x12\x0e\n\x06margin\x18\x06 \x01(\t\x12\r\n\x05price\x18\x07 \x01(\t\x12\x10\n\x08quantity\x18\x08 \x01(\t\x12\x19\n\x11unfilled_quantity\x18\t \x01(\t\x12\x15\n\rtrigger_price\x18\n \x01(\t\x12\x15\n\rfee_recipient\x18\x0b \x01(\t\x12\r\n\x05state\x18\x0c \x01(\t\x12\x12\n\ncreated_at\x18\r \x01(\x12\x12\x12\n\nupdated_at\x18\x0e \x01(\x12\x12\x14\n\x0corder_number\x18\x0f \x01(\x12\x12\x12\n\norder_type\x18\x10 \x01(\t\x12\x16\n\x0eis_conditional\x18\x11 \x01(\x08\x12\x12\n\ntrigger_at\x18\x12 \x01(\x04\x12\x19\n\x11placed_order_hash\x18\x13 \x01(\t\x12\x16\n\x0e\x65xecution_type\x18\x14 \x01(\t\"\xca\x01\n\x10PositionsRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x12\n\nstart_time\x18\x05 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\x12\x12\x12\n\nmarket_ids\x18\x07 \x03(\t\x12\x11\n\tdirection\x18\x08 \x01(\t\x12\"\n\x1asubaccount_total_positions\x18\t \x01(\x08\"\x98\x01\n\x11PositionsResponse\x12H\n\tpositions\x18\x01 \x03(\x0b\x32\x35.injective_derivative_exchange_rpc.DerivativePosition\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\x97\x02\n\x12\x44\x65rivativePosition\x12\x0e\n\x06ticker\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x15\n\rsubaccount_id\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\t\x12\x13\n\x0b\x65ntry_price\x18\x06 \x01(\t\x12\x0e\n\x06margin\x18\x07 \x01(\t\x12\x19\n\x11liquidation_price\x18\x08 \x01(\t\x12\x12\n\nmark_price\x18\t \x01(\t\x12&\n\x1e\x61ggregate_reduce_only_quantity\x18\x0b \x01(\t\x12\x12\n\nupdated_at\x18\x0c \x01(\x12\x12\x12\n\ncreated_at\x18\r \x01(\x12\"L\n\x1aLiquidablePositionsRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0c\n\x04skip\x18\x02 \x01(\x04\x12\r\n\x05limit\x18\x03 \x01(\x11\"g\n\x1bLiquidablePositionsResponse\x12H\n\tpositions\x18\x01 \x03(\x0b\x32\x35.injective_derivative_exchange_rpc.DerivativePosition\"\x85\x01\n\x16\x46undingPaymentsRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\x12\x12\x12\n\nmarket_ids\x18\x06 \x03(\t\"\x99\x01\n\x17\x46undingPaymentsResponse\x12\x43\n\x08payments\x18\x01 \x03(\x0b\x32\x31.injective_derivative_exchange_rpc.FundingPayment\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"]\n\x0e\x46undingPayment\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x12\"W\n\x13\x46undingRatesRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0c\n\x04skip\x18\x02 \x01(\x04\x12\r\n\x05limit\x18\x03 \x01(\x11\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x12\"\x98\x01\n\x14\x46undingRatesResponse\x12\x45\n\rfunding_rates\x18\x01 \x03(\x0b\x32..injective_derivative_exchange_rpc.FundingRate\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"A\n\x0b\x46undingRate\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x0c\n\x04rate\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"n\n\x16StreamPositionsRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x12\n\nmarket_ids\x18\x03 \x03(\t\x12\x16\n\x0esubaccount_ids\x18\x04 \x03(\t\"u\n\x17StreamPositionsResponse\x12G\n\x08position\x18\x01 \x01(\x0b\x32\x35.injective_derivative_exchange_rpc.DerivativePosition\x12\x11\n\ttimestamp\x18\x02 \x01(\x12\"\x91\x02\n\x13StreamOrdersRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x12\n\norder_side\x18\x02 \x01(\t\x12\x15\n\rsubaccount_id\x18\x03 \x01(\t\x12\x0c\n\x04skip\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x11\x12\x12\n\nstart_time\x18\x06 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x12\x12\x12\n\nmarket_ids\x18\x08 \x03(\t\x12\x16\n\x0eis_conditional\x18\t \x01(\t\x12\x12\n\norder_type\x18\n \x01(\t\x12\x18\n\x10include_inactive\x18\x0b \x01(\x08\x12\x1f\n\x17subaccount_total_orders\x18\x0c \x01(\x08\"\x89\x01\n\x14StreamOrdersResponse\x12\x46\n\x05order\x18\x01 \x01(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeLimitOrder\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"\xec\x01\n\rTradesRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\"\x8f\x01\n\x0eTradesResponse\x12\x42\n\x06trades\x18\x01 \x03(\x0b\x32\x32.injective_derivative_exchange_rpc.DerivativeTrade\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\xc2\x02\n\x0f\x44\x65rivativeTrade\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x15\n\rsubaccount_id\x18\x02 \x01(\t\x12\x11\n\tmarket_id\x18\x03 \x01(\t\x12\x1c\n\x14trade_execution_type\x18\x04 \x01(\t\x12\x16\n\x0eis_liquidation\x18\x05 \x01(\x08\x12H\n\x0eposition_delta\x18\x06 \x01(\x0b\x32\x30.injective_derivative_exchange_rpc.PositionDelta\x12\x0e\n\x06payout\x18\x07 \x01(\t\x12\x0b\n\x03\x66\x65\x65\x18\x08 \x01(\t\x12\x13\n\x0b\x65xecuted_at\x18\t \x01(\x12\x12\x15\n\rfee_recipient\x18\n \x01(\t\x12\x10\n\x08trade_id\x18\x0b \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x0c \x01(\t\"w\n\rPositionDelta\x12\x17\n\x0ftrade_direction\x18\x01 \x01(\t\x12\x17\n\x0f\x65xecution_price\x18\x02 \x01(\t\x12\x1a\n\x12\x65xecution_quantity\x18\x03 \x01(\t\x12\x18\n\x10\x65xecution_margin\x18\x04 \x01(\t\"\xf2\x01\n\x13StreamTradesRequest\x12\x11\n\tmarket_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65xecution_side\x18\x02 \x01(\t\x12\x11\n\tdirection\x18\x03 \x01(\t\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x12\n\nmarket_ids\x18\t \x03(\t\x12\x16\n\x0esubaccount_ids\x18\n \x03(\t\x12\x17\n\x0f\x65xecution_types\x18\x0b \x03(\t\"\x84\x01\n\x14StreamTradesResponse\x12\x41\n\x05trade\x18\x01 \x01(\x0b\x32\x32.injective_derivative_exchange_rpc.DerivativeTrade\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\"d\n\x1bSubaccountOrdersListRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\"\xa2\x01\n\x1cSubaccountOrdersListResponse\x12G\n\x06orders\x18\x01 \x03(\x0b\x32\x37.injective_derivative_exchange_rpc.DerivativeLimitOrder\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\x8f\x01\n\x1bSubaccountTradesListRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x16\n\x0e\x65xecution_type\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x0c\n\x04skip\x18\x05 \x01(\x04\x12\r\n\x05limit\x18\x06 \x01(\x11\"b\n\x1cSubaccountTradesListResponse\x12\x42\n\x06trades\x18\x01 \x03(\x0b\x32\x32.injective_derivative_exchange_rpc.DerivativeTrade\"\x93\x02\n\x14OrdersHistoryRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x0c\n\x04skip\x18\x03 \x01(\x04\x12\r\n\x05limit\x18\x04 \x01(\x11\x12\x13\n\x0border_types\x18\x05 \x03(\t\x12\x11\n\tdirection\x18\x06 \x01(\t\x12\x12\n\nstart_time\x18\x07 \x01(\x12\x12\x10\n\x08\x65nd_time\x18\x08 \x01(\x12\x12\x16\n\x0eis_conditional\x18\t \x01(\t\x12\x12\n\norder_type\x18\n \x01(\t\x12\r\n\x05state\x18\x0b \x01(\t\x12\x17\n\x0f\x65xecution_types\x18\x0c \x03(\t\x12\x12\n\nmarket_ids\x18\r \x03(\t\"\x9d\x01\n\x15OrdersHistoryResponse\x12I\n\x06orders\x18\x01 \x03(\x0b\x32\x39.injective_derivative_exchange_rpc.DerivativeOrderHistory\x12\x39\n\x06paging\x18\x02 \x01(\x0b\x32).injective_derivative_exchange_rpc.Paging\"\x9f\x03\n\x16\x44\x65rivativeOrderHistory\x12\x12\n\norder_hash\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x11\n\tis_active\x18\x03 \x01(\x08\x12\x15\n\rsubaccount_id\x18\x04 \x01(\t\x12\x16\n\x0e\x65xecution_type\x18\x05 \x01(\t\x12\x12\n\norder_type\x18\x06 \x01(\t\x12\r\n\x05price\x18\x07 \x01(\t\x12\x15\n\rtrigger_price\x18\x08 \x01(\t\x12\x10\n\x08quantity\x18\t \x01(\t\x12\x17\n\x0f\x66illed_quantity\x18\n \x01(\t\x12\r\n\x05state\x18\x0b \x01(\t\x12\x12\n\ncreated_at\x18\x0c \x01(\x12\x12\x12\n\nupdated_at\x18\r \x01(\x12\x12\x16\n\x0eis_reduce_only\x18\x0e \x01(\x08\x12\x11\n\tdirection\x18\x0f \x01(\t\x12\x16\n\x0eis_conditional\x18\x10 \x01(\x08\x12\x12\n\ntrigger_at\x18\x11 \x01(\x04\x12\x19\n\x11placed_order_hash\x18\x12 \x01(\t\x12\x0e\n\x06margin\x18\x13 \x01(\t\"\x96\x01\n\x1aStreamOrdersHistoryRequest\x12\x15\n\rsubaccount_id\x18\x01 \x01(\t\x12\x11\n\tmarket_id\x18\x02 \x01(\t\x12\x13\n\x0border_types\x18\x03 \x03(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\r\n\x05state\x18\x05 \x01(\t\x12\x17\n\x0f\x65xecution_types\x18\x06 \x03(\t\"\x92\x01\n\x1bStreamOrdersHistoryResponse\x12H\n\x05order\x18\x01 \x01(\x0b\x32\x39.injective_derivative_exchange_rpc.DerivativeOrderHistory\x12\x16\n\x0eoperation_type\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x12\x32\xc7\x1a\n\x1eInjectiveDerivativeExchangeRPC\x12p\n\x07Markets\x12\x31.injective_derivative_exchange_rpc.MarketsRequest\x1a\x32.injective_derivative_exchange_rpc.MarketsResponse\x12m\n\x06Market\x12\x30.injective_derivative_exchange_rpc.MarketRequest\x1a\x31.injective_derivative_exchange_rpc.MarketResponse\x12\x81\x01\n\x0cStreamMarket\x12\x36.injective_derivative_exchange_rpc.StreamMarketRequest\x1a\x37.injective_derivative_exchange_rpc.StreamMarketResponse0\x01\x12\x97\x01\n\x14\x42inaryOptionsMarkets\x12>.injective_derivative_exchange_rpc.BinaryOptionsMarketsRequest\x1a?.injective_derivative_exchange_rpc.BinaryOptionsMarketsResponse\x12\x94\x01\n\x13\x42inaryOptionsMarket\x12=.injective_derivative_exchange_rpc.BinaryOptionsMarketRequest\x1a>.injective_derivative_exchange_rpc.BinaryOptionsMarketResponse\x12v\n\tOrderbook\x12\x33.injective_derivative_exchange_rpc.OrderbookRequest\x1a\x34.injective_derivative_exchange_rpc.OrderbookResponse\x12|\n\x0bOrderbookV2\x12\x35.injective_derivative_exchange_rpc.OrderbookV2Request\x1a\x36.injective_derivative_exchange_rpc.OrderbookV2Response\x12y\n\nOrderbooks\x12\x34.injective_derivative_exchange_rpc.OrderbooksRequest\x1a\x35.injective_derivative_exchange_rpc.OrderbooksResponse\x12\x7f\n\x0cOrderbooksV2\x12\x36.injective_derivative_exchange_rpc.OrderbooksV2Request\x1a\x37.injective_derivative_exchange_rpc.OrderbooksV2Response\x12\x8a\x01\n\x0fStreamOrderbook\x12\x39.injective_derivative_exchange_rpc.StreamOrderbookRequest\x1a:.injective_derivative_exchange_rpc.StreamOrderbookResponse0\x01\x12\x90\x01\n\x11StreamOrderbookV2\x12;.injective_derivative_exchange_rpc.StreamOrderbookV2Request\x1a<.injective_derivative_exchange_rpc.StreamOrderbookV2Response0\x01\x12\x9c\x01\n\x15StreamOrderbookUpdate\x12?.injective_derivative_exchange_rpc.StreamOrderbookUpdateRequest\x1a@.injective_derivative_exchange_rpc.StreamOrderbookUpdateResponse0\x01\x12m\n\x06Orders\x12\x30.injective_derivative_exchange_rpc.OrdersRequest\x1a\x31.injective_derivative_exchange_rpc.OrdersResponse\x12v\n\tPositions\x12\x33.injective_derivative_exchange_rpc.PositionsRequest\x1a\x34.injective_derivative_exchange_rpc.PositionsResponse\x12\x94\x01\n\x13LiquidablePositions\x12=.injective_derivative_exchange_rpc.LiquidablePositionsRequest\x1a>.injective_derivative_exchange_rpc.LiquidablePositionsResponse\x12\x88\x01\n\x0f\x46undingPayments\x12\x39.injective_derivative_exchange_rpc.FundingPaymentsRequest\x1a:.injective_derivative_exchange_rpc.FundingPaymentsResponse\x12\x7f\n\x0c\x46undingRates\x12\x36.injective_derivative_exchange_rpc.FundingRatesRequest\x1a\x37.injective_derivative_exchange_rpc.FundingRatesResponse\x12\x8a\x01\n\x0fStreamPositions\x12\x39.injective_derivative_exchange_rpc.StreamPositionsRequest\x1a:.injective_derivative_exchange_rpc.StreamPositionsResponse0\x01\x12\x81\x01\n\x0cStreamOrders\x12\x36.injective_derivative_exchange_rpc.StreamOrdersRequest\x1a\x37.injective_derivative_exchange_rpc.StreamOrdersResponse0\x01\x12m\n\x06Trades\x12\x30.injective_derivative_exchange_rpc.TradesRequest\x1a\x31.injective_derivative_exchange_rpc.TradesResponse\x12\x81\x01\n\x0cStreamTrades\x12\x36.injective_derivative_exchange_rpc.StreamTradesRequest\x1a\x37.injective_derivative_exchange_rpc.StreamTradesResponse0\x01\x12\x97\x01\n\x14SubaccountOrdersList\x12>.injective_derivative_exchange_rpc.SubaccountOrdersListRequest\x1a?.injective_derivative_exchange_rpc.SubaccountOrdersListResponse\x12\x97\x01\n\x14SubaccountTradesList\x12>.injective_derivative_exchange_rpc.SubaccountTradesListRequest\x1a?.injective_derivative_exchange_rpc.SubaccountTradesListResponse\x12\x82\x01\n\rOrdersHistory\x12\x37.injective_derivative_exchange_rpc.OrdersHistoryRequest\x1a\x38.injective_derivative_exchange_rpc.OrdersHistoryResponse\x12\x96\x01\n\x13StreamOrdersHistory\x12=.injective_derivative_exchange_rpc.StreamOrdersHistoryRequest\x1a>.injective_derivative_exchange_rpc.StreamOrdersHistoryResponse0\x01\x42&Z$/injective_derivative_exchange_rpcpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exchange.injective_derivative_exchange_rpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$/injective_derivative_exchange_rpcpb'
  _MARKETSREQUEST._serialized_start=87
  _MARKETSREQUEST._serialized_end=147
  _MARKETSRESPONSE._serialized_start=149
  _MARKETSRESPONSE._serialized_end=240
  _DERIVATIVEMARKETINFO._serialized_start=243
  _DERIVATIVEMARKETINFO._serialized_end=1010
  _TOKENMETA._serialized_start=1012
  _TOKENMETA._serialized_end=1122
  _PERPETUALMARKETINFO._serialized_start=1125
  _PERPETUALMARKETINFO._serialized_end=1267
  _PERPETUALMARKETFUNDING._serialized_start=1269
  _PERPETUALMARKETFUNDING._serialized_end=1371
  _EXPIRYFUTURESMARKETINFO._serialized_start=1373
  _EXPIRYFUTURESMARKETINFO._serialized_end=1454
  _MARKETREQUEST._serialized_start=1456
  _MARKETREQUEST._serialized_end=1490
  _MARKETRESPONSE._serialized_start=1492
  _MARKETRESPONSE._serialized_end=1581
  _STREAMMARKETREQUEST._serialized_start=1583
  _STREAMMARKETREQUEST._serialized_end=1624
  _STREAMMARKETRESPONSE._serialized_start=1627
  _STREAMMARKETRESPONSE._serialized_end=1765
  _BINARYOPTIONSMARKETSREQUEST._serialized_start=1767
  _BINARYOPTIONSMARKETSREQUEST._serialized_end=1869
  _BINARYOPTIONSMARKETSRESPONSE._serialized_start=1872
  _BINARYOPTIONSMARKETSRESPONSE._serialized_end=2038
  _BINARYOPTIONSMARKETINFO._serialized_start=2041
  _BINARYOPTIONSMARKETINFO._serialized_end=2540
  _PAGING._serialized_start=2542
  _PAGING._serialized_end=2620
  _BINARYOPTIONSMARKETREQUEST._serialized_start=2622
  _BINARYOPTIONSMARKETREQUEST._serialized_end=2669
  _BINARYOPTIONSMARKETRESPONSE._serialized_start=2671
  _BINARYOPTIONSMARKETRESPONSE._serialized_end=2776
  _ORDERBOOKREQUEST._serialized_start=2778
  _ORDERBOOKREQUEST._serialized_end=2815
  _ORDERBOOKRESPONSE._serialized_start=2817
  _ORDERBOOKRESPONSE._serialized_end=2916
  _DERIVATIVELIMITORDERBOOK._serialized_start=2919
  _DERIVATIVELIMITORDERBOOK._serialized_end=3087
  _PRICELEVEL._serialized_start=3089
  _PRICELEVEL._serialized_end=3153
  _ORDERBOOKV2REQUEST._serialized_start=3155
  _ORDERBOOKV2REQUEST._serialized_end=3194
  _ORDERBOOKV2RESPONSE._serialized_start=3196
  _ORDERBOOKV2RESPONSE._serialized_end=3299
  _DERIVATIVELIMITORDERBOOKV2._serialized_start=3302
  _DERIVATIVELIMITORDERBOOKV2._serialized_end=3490
  _ORDERBOOKSREQUEST._serialized_start=3492
  _ORDERBOOKSREQUEST._serialized_end=3531
  _ORDERBOOKSRESPONSE._serialized_start=3533
  _ORDERBOOKSRESPONSE._serialized_end=3640
  _SINGLEDERIVATIVELIMITORDERBOOK._serialized_start=3643
  _SINGLEDERIVATIVELIMITORDERBOOK._serialized_end=3774
  _ORDERBOOKSV2REQUEST._serialized_start=3776
  _ORDERBOOKSV2REQUEST._serialized_end=3817
  _ORDERBOOKSV2RESPONSE._serialized_start=3819
  _ORDERBOOKSV2RESPONSE._serialized_end=3930
  _SINGLEDERIVATIVELIMITORDERBOOKV2._serialized_start=3933
  _SINGLEDERIVATIVELIMITORDERBOOKV2._serialized_end=4068
  _STREAMORDERBOOKREQUEST._serialized_start=4070
  _STREAMORDERBOOKREQUEST._serialized_end=4114
  _STREAMORDERBOOKRESPONSE._serialized_start=4117
  _STREAMORDERBOOKRESPONSE._serialized_end=4284
  _STREAMORDERBOOKV2REQUEST._serialized_start=4286
  _STREAMORDERBOOKV2REQUEST._serialized_end=4332
  _STREAMORDERBOOKV2RESPONSE._serialized_start=4335
  _STREAMORDERBOOKV2RESPONSE._serialized_end=4506
  _STREAMORDERBOOKUPDATEREQUEST._serialized_start=4508
  _STREAMORDERBOOKUPDATEREQUEST._serialized_end=4558
  _STREAMORDERBOOKUPDATERESPONSE._serialized_start=4561
  _STREAMORDERBOOKUPDATERESPONSE._serialized_end=4745
  _ORDERBOOKLEVELUPDATES._serialized_start=4748
  _ORDERBOOKLEVELUPDATES._serialized_end=4963
  _PRICELEVELUPDATE._serialized_start=4965
  _PRICELEVELUPDATE._serialized_end=5054
  _ORDERSREQUEST._serialized_start=5057
  _ORDERSREQUEST._serialized_end=5324
  _ORDERSRESPONSE._serialized_start=5327
  _ORDERSRESPONSE._serialized_end=5475
  _DERIVATIVELIMITORDER._serialized_start=5478
  _DERIVATIVELIMITORDER._serialized_end=5920
  _POSITIONSREQUEST._serialized_start=5923
  _POSITIONSREQUEST._serialized_end=6125
  _POSITIONSRESPONSE._serialized_start=6128
  _POSITIONSRESPONSE._serialized_end=6280
  _DERIVATIVEPOSITION._serialized_start=6283
  _DERIVATIVEPOSITION._serialized_end=6562
  _LIQUIDABLEPOSITIONSREQUEST._serialized_start=6564
  _LIQUIDABLEPOSITIONSREQUEST._serialized_end=6640
  _LIQUIDABLEPOSITIONSRESPONSE._serialized_start=6642
  _LIQUIDABLEPOSITIONSRESPONSE._serialized_end=6745
  _FUNDINGPAYMENTSREQUEST._serialized_start=6748
  _FUNDINGPAYMENTSREQUEST._serialized_end=6881
  _FUNDINGPAYMENTSRESPONSE._serialized_start=6884
  _FUNDINGPAYMENTSRESPONSE._serialized_end=7037
  _FUNDINGPAYMENT._serialized_start=7039
  _FUNDINGPAYMENT._serialized_end=7132
  _FUNDINGRATESREQUEST._serialized_start=7134
  _FUNDINGRATESREQUEST._serialized_end=7221
  _FUNDINGRATESRESPONSE._serialized_start=7224
  _FUNDINGRATESRESPONSE._serialized_end=7376
  _FUNDINGRATE._serialized_start=7378
  _FUNDINGRATE._serialized_end=7443
  _STREAMPOSITIONSREQUEST._serialized_start=7445
  _STREAMPOSITIONSREQUEST._serialized_end=7555
  _STREAMPOSITIONSRESPONSE._serialized_start=7557
  _STREAMPOSITIONSRESPONSE._serialized_end=7674
  _STREAMORDERSREQUEST._serialized_start=7677
  _STREAMORDERSREQUEST._serialized_end=7950
  _STREAMORDERSRESPONSE._serialized_start=7953
  _STREAMORDERSRESPONSE._serialized_end=8090
  _TRADESREQUEST._serialized_start=8093
  _TRADESREQUEST._serialized_end=8329
  _TRADESRESPONSE._serialized_start=8332
  _TRADESRESPONSE._serialized_end=8475
  _DERIVATIVETRADE._serialized_start=8478
  _DERIVATIVETRADE._serialized_end=8800
  _POSITIONDELTA._serialized_start=8802
  _POSITIONDELTA._serialized_end=8921
  _STREAMTRADESREQUEST._serialized_start=8924
  _STREAMTRADESREQUEST._serialized_end=9166
  _STREAMTRADESRESPONSE._serialized_start=9169
  _STREAMTRADESRESPONSE._serialized_end=9301
  _SUBACCOUNTORDERSLISTREQUEST._serialized_start=9303
  _SUBACCOUNTORDERSLISTREQUEST._serialized_end=9403
  _SUBACCOUNTORDERSLISTRESPONSE._serialized_start=9406
  _SUBACCOUNTORDERSLISTRESPONSE._serialized_end=9568
  _SUBACCOUNTTRADESLISTREQUEST._serialized_start=9571
  _SUBACCOUNTTRADESLISTREQUEST._serialized_end=9714
  _SUBACCOUNTTRADESLISTRESPONSE._serialized_start=9716
  _SUBACCOUNTTRADESLISTRESPONSE._serialized_end=9814
  _ORDERSHISTORYREQUEST._serialized_start=9817
  _ORDERSHISTORYREQUEST._serialized_end=10092
  _ORDERSHISTORYRESPONSE._serialized_start=10095
  _ORDERSHISTORYRESPONSE._serialized_end=10252
  _DERIVATIVEORDERHISTORY._serialized_start=10255
  _DERIVATIVEORDERHISTORY._serialized_end=10670
  _STREAMORDERSHISTORYREQUEST._serialized_start=10673
  _STREAMORDERSHISTORYREQUEST._serialized_end=10823
  _STREAMORDERSHISTORYRESPONSE._serialized_start=10826
  _STREAMORDERSHISTORYRESPONSE._serialized_end=10972
  _INJECTIVEDERIVATIVEEXCHANGERPC._serialized_start=10975
  _INJECTIVEDERIVATIVEEXCHANGERPC._serialized_end=14374
# @@protoc_insertion_point(module_scope)
