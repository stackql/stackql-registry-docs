---
title: countries
hide_title: false
hide_table_of_contents: false
keywords:
  - countries
  - dfareporting
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
<tr><td><b>Name</b></td><td><code>countries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.countries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of this country. |
| `sslEnabled` | `boolean` | Whether ad serving supports secure servers in this country. |
| `countryCode` | `string` | Country code. |
| `dartId` | `string` | DART ID of this country. This is the ID used for targeting and generating reports. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#country". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dartId, profileId` | Gets one country by ID. |
| `list` | `SELECT` | `profileId` | Retrieves a list of countries. |
