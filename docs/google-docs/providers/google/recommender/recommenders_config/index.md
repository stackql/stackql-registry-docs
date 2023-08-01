---
title: recommenders_config
hide_title: false
hide_table_of_contents: false
keywords:
  - recommenders_config
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
<tr><td><b>Name</b></td><td><code>recommenders_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.recommenders_config</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_recommenders_get_config` | `EXEC` | `billingAccountsId, locationsId, recommendersId` | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| `billing_accounts_locations_recommenders_update_config` | `EXEC` | `billingAccountsId, locationsId, recommendersId` | Updates a Recommender Config. This will create a new revision of the config. |
| `organizations_locations_recommenders_get_config` | `EXEC` | `locationsId, organizationsId, recommendersId` | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| `organizations_locations_recommenders_update_config` | `EXEC` | `locationsId, organizationsId, recommendersId` | Updates a Recommender Config. This will create a new revision of the config. |
| `projects_locations_recommenders_get_config` | `EXEC` | `locationsId, projectsId, recommendersId` | Gets the requested Recommender Config. There is only one instance of the config for each Recommender. |
| `projects_locations_recommenders_update_config` | `EXEC` | `locationsId, projectsId, recommendersId` | Updates a Recommender Config. This will create a new revision of the config. |
