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
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.datastores" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_analytics_datastores_get" /> | `SELECT` | <CopyableCode code="datastoresId, organizationsId" /> | Get a Datastore |
| <CopyableCode code="organizations_analytics_datastores_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | List Datastores |
| <CopyableCode code="organizations_analytics_datastores_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Create a Datastore for an org |
| <CopyableCode code="organizations_analytics_datastores_delete" /> | `DELETE` | <CopyableCode code="datastoresId, organizationsId" /> | Delete a Datastore from an org. |
| <CopyableCode code="organizations_analytics_datastores_test" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage |
| <CopyableCode code="organizations_analytics_datastores_update" /> | `EXEC` | <CopyableCode code="datastoresId, organizationsId" /> | Update a Datastore |
