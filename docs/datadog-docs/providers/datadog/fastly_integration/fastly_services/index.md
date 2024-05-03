---
title: fastly_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fastly_services
  - fastly_integration
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
<tr><td><b>Name</b></td><td><code>fastly_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.fastly_integration.fastly_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the Fastly service. |
| <CopyableCode code="attributes" /> | `object` | Attributes object for Fastly service requests. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for this API. Should always be `fastly-services`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_fastly_service" /> | `SELECT` | <CopyableCode code="account_id, service_id, dd_site" /> | Get a Fastly service for an account. |
| <CopyableCode code="list_fastly_services" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | List Fastly services for an account. |
| <CopyableCode code="create_fastly_service" /> | `INSERT` | <CopyableCode code="account_id, data__data, dd_site" /> | Create a Fastly service for an account. |
| <CopyableCode code="delete_fastly_service" /> | `DELETE` | <CopyableCode code="account_id, service_id, dd_site" /> | Delete a Fastly service for an account. |
| <CopyableCode code="_get_fastly_service" /> | `EXEC` | <CopyableCode code="account_id, service_id, dd_site" /> | Get a Fastly service for an account. |
| <CopyableCode code="_list_fastly_services" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | List Fastly services for an account. |
| <CopyableCode code="update_fastly_service" /> | `EXEC` | <CopyableCode code="account_id, service_id, data__data, dd_site" /> | Update a Fastly service for an account. |
