---
title: service_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_definitions
  - service_definition
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.service_definition.service_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Service definition id. |
| <CopyableCode code="attributes" /> | `object` | Service definition attributes. |
| <CopyableCode code="type" /> | `string` | Service definition type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_service_definition" /> | `SELECT` | <CopyableCode code="service_name, dd_site" /> | Get a single service definition from the Datadog Service Catalog. |
| <CopyableCode code="list_service_definitions" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get a list of all service definitions from the Datadog Service Catalog. |
| <CopyableCode code="create_or_update_service_definitions" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create or update service definition in the Datadog Service Catalog. |
| <CopyableCode code="delete_service_definition" /> | `DELETE` | <CopyableCode code="service_name, dd_site" /> | Delete a single service definition in the Datadog Service Catalog. |
| <CopyableCode code="_get_service_definition" /> | `EXEC` | <CopyableCode code="service_name, dd_site" /> | Get a single service definition from the Datadog Service Catalog. |
| <CopyableCode code="_list_service_definitions" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get a list of all service definitions from the Datadog Service Catalog. |
