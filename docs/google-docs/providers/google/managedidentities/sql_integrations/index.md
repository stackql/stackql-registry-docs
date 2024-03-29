---
title: sql_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_integrations
  - managedidentities
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
<tr><td><b>Name</b></td><td><code>sql_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.sql_integrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the SQL integration in the form of `projects/&#123;project_id&#125;/locations/global/domains/&#123;domain_name&#125;/sqlIntegrations/&#123;sql_integration&#125;` |
| `sqlInstance` | `string` | The full resource name of an integrated SQL instance |
| `state` | `string` | Output only. The current state of the SQL integration. |
| `updateTime` | `string` | Output only. The time the SQL integration was updated. |
| `createTime` | `string` | Output only. The time the SQL integration was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainsId, projectsId, sqlIntegrationsId` | Gets details of a single sqlIntegration. |
| `list` | `SELECT` | `domainsId, projectsId` | Lists SqlIntegrations in a given domain. |
| `_list` | `EXEC` | `domainsId, projectsId` | Lists SqlIntegrations in a given domain. |
