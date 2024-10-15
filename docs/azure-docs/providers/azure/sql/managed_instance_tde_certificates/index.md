---
title: managed_instance_tde_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_tde_certificates
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_instance_tde_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_instance_tde_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instance_tde_certificates" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Creates a TDE certificate for a given server. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_instance_tde_certificates</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.sql.managed_instance_tde_certificates (
managedInstanceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ managedInstanceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: privateBlob
          value: string
        - name: certPassword
          value: string

```
</TabItem>
</Tabs>
