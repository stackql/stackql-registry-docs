---
title: conversion__by_customer_id
hide_title: false
hide_table_of_contents: false
keywords:
  - conversion__by_customer_id
  - doubleclicksearch
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversion__by_customer_id</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.doubleclicksearch.conversion__by_customer_id</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `conversion` | `array` | The conversions being requested. |
| `kind` | `string` | Identifies this as a ConversionList resource. Value: the fixed string doubleclicksearch#conversionList. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `conversion_getByCustomerId` | `SELECT` | `customerId, endDate, rowCount, startDate, startRow` |
