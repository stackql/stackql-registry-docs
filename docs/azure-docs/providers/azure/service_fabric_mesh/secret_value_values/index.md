---
title: secret_value_values
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_value_values
  - service_fabric_mesh
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>secret_value_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_value_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.secret_value_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `string` | The actual value of the secret. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId" /> | Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation. |

## `SELECT` examples

Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation.


```sql
SELECT
value
FROM azure.service_fabric_mesh.secret_value_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND secretResourceName = '{{ secretResourceName }}'
AND secretValueResourceName = '{{ secretValueResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```