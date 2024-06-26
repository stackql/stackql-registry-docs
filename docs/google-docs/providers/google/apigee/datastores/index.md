---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.datastores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createTime" /> | `string` | Output only. Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| <CopyableCode code="datastoreConfig" /> | `object` | Configuration detail for datastore |
| <CopyableCode code="displayName" /> | `string` | Required. Display name in UI |
| <CopyableCode code="lastUpdateTime" /> | `string` | Output only. Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| <CopyableCode code="org" /> | `string` | Output only. Organization that the datastore belongs to |
| <CopyableCode code="self" /> | `string` | Output only. Resource link of Datastore. Example: `/organizations/&#123;org&#125;/analytics/datastores/&#123;uuid&#125;` |
| <CopyableCode code="targetType" /> | `string` | Destination storage type. Supported types `gcs` or `bigquery`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_analytics_datastores_get" /> | `SELECT` | <CopyableCode code="datastoresId, organizationsId" /> | Get a Datastore |
| <CopyableCode code="organizations_analytics_datastores_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | List Datastores |
| <CopyableCode code="organizations_analytics_datastores_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Create a Datastore for an org |
| <CopyableCode code="organizations_analytics_datastores_delete" /> | `DELETE` | <CopyableCode code="datastoresId, organizationsId" /> | Delete a Datastore from an org. |
| <CopyableCode code="organizations_analytics_datastores_update" /> | `UPDATE` | <CopyableCode code="datastoresId, organizationsId" /> | Update a Datastore |
| <CopyableCode code="organizations_analytics_datastores_test" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage |
