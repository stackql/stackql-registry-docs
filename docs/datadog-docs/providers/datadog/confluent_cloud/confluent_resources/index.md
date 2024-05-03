---
title: confluent_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - confluent_resources
  - confluent_cloud
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
<tr><td><b>Name</b></td><td><code>confluent_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.confluent_cloud.confluent_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID associated with the Confluent resource. |
| <CopyableCode code="attributes" /> | `object` | Model representation of a Confluent Cloud resource. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for this request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_confluent_resource" /> | `SELECT` | <CopyableCode code="account_id, resource_id, dd_site" /> | Get a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| <CopyableCode code="list_confluent_resource" /> | `SELECT` | <CopyableCode code="account_id, dd_site" /> | Get a Confluent resource for the account associated with the provided ID. |
| <CopyableCode code="create_confluent_resource" /> | `INSERT` | <CopyableCode code="account_id, data__data, dd_site" /> | Create a Confluent resource for the account associated with the provided ID. |
| <CopyableCode code="delete_confluent_resource" /> | `DELETE` | <CopyableCode code="account_id, resource_id, dd_site" /> | Delete a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| <CopyableCode code="_get_confluent_resource" /> | `EXEC` | <CopyableCode code="account_id, resource_id, dd_site" /> | Get a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| <CopyableCode code="_list_confluent_resource" /> | `EXEC` | <CopyableCode code="account_id, dd_site" /> | Get a Confluent resource for the account associated with the provided ID. |
| <CopyableCode code="update_confluent_resource" /> | `EXEC` | <CopyableCode code="account_id, resource_id, data__data, dd_site" /> | Update a Confluent resource with the provided resource id for the account associated with the provided account ID. |
