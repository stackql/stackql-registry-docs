---
title: keyvaluemaps
hide_title: false
hide_table_of_contents: false
keywords:
  - keyvaluemaps
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
<tr><td><b>Name</b></td><td><code>keyvaluemaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.keyvaluemaps" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="apisId, organizationsId" /> | Creates a key value map in an API proxy. |
| <CopyableCode code="organizations_environments_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a key value map in an environment. |
| <CopyableCode code="organizations_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a key value map in an organization. |
| <CopyableCode code="organizations_apis_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="apisId, keyvaluemapsId, organizationsId" /> | Deletes a key value map from an API proxy. |
| <CopyableCode code="organizations_environments_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="environmentsId, keyvaluemapsId, organizationsId" /> | Deletes a key value map from an environment. |
| <CopyableCode code="organizations_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="keyvaluemapsId, organizationsId" /> | Deletes a key value map from an organization. |
