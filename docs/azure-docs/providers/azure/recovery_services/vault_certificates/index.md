---
title: vault_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - vault_certificates
  - recovery_services
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

Creates, updates, deletes, gets or lists a <code>vault_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vault_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.vault_certificates" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="certificateName, resourceGroupName, subscriptionId, vaultName" /> | Uploads a certificate for a resource. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vault_certificates</code> resource.

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
INSERT INTO azure.recovery_services.vault_certificates (
certificateName,
resourceGroupName,
subscriptionId,
vaultName,
properties
)
SELECT 
'{{ certificateName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
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
        - name: authType
          value: string
        - name: certificate
          value: string

```
</TabItem>
</Tabs>
