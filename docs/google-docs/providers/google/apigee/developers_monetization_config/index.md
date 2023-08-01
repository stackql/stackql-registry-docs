---
title: developers_monetization_config
hide_title: false
hide_table_of_contents: false
keywords:
  - developers_monetization_config
  - apigee
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>developers_monetization_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.developers_monetization_config</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_developers_get_monetization_config` | `SELECT` | `developersId, organizationsId` | Gets the monetization configuration for the developer. |
| `organizations_developers_update_monetization_config` | `EXEC` | `developersId, organizationsId` | Updates the monetization configuration for the developer. |
