---
title: insight_types_config
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_types_config
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
<tr><td><b>Name</b></td><td><code>insight_types_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.insight_types_config</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_insight_types_get_config` | `EXEC` | `billingAccountsId, insightTypesId, locationsId` | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| `billing_accounts_locations_insight_types_update_config` | `EXEC` | `billingAccountsId, insightTypesId, locationsId` | Updates an InsightTypeConfig change. This will create a new revision of the config. |
| `organizations_locations_insight_types_get_config` | `EXEC` | `insightTypesId, locationsId, organizationsId` | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| `organizations_locations_insight_types_update_config` | `EXEC` | `insightTypesId, locationsId, organizationsId` | Updates an InsightTypeConfig change. This will create a new revision of the config. |
| `projects_locations_insight_types_get_config` | `EXEC` | `insightTypesId, locationsId, projectsId` | Gets the requested InsightTypeConfig. There is only one instance of the config for each InsightType. |
| `projects_locations_insight_types_update_config` | `EXEC` | `insightTypesId, locationsId, projectsId` | Updates an InsightTypeConfig change. This will create a new revision of the config. |
