---
title: insight_types
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_types
  - recommender
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
<tr><td><b>Name</b></td><td><code>insight_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.insight_types</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `billingAccounts_locations_insightTypes_updateConfig` | `EXEC` | `billingAccountsId, insightTypesId, locationsId` |
| `organizations_locations_insightTypes_updateConfig` | `EXEC` | `insightTypesId, locationsId, organizationsId` |
| `projects_locations_insightTypes_updateConfig` | `EXEC` | `insightTypesId, locationsId, projectsId` |
