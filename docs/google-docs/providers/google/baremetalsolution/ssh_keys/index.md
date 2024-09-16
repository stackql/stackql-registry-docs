---
title: ssh_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_keys
  - baremetalsolution
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

Creates, updates, deletes, gets or lists a <code>ssh_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.ssh_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of this SSH key. Currently, the only valid value for the location is "global". |
| <CopyableCode code="publicKey" /> | `string` | The public SSH key. This must be in OpenSSH .authorized_keys format. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the public SSH keys registered for the specified project. These SSH keys are used only for the interactive serial console feature. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Register a public SSH key in the specified project for use with the interactive serial console feature. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sshKeysId" /> | Deletes a public SSH key registered in the specified project. |

## `SELECT` examples

Lists the public SSH keys registered for the specified project. These SSH keys are used only for the interactive serial console feature.

```sql
SELECT
name,
publicKey
FROM google.baremetalsolution.ssh_keys
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ssh_keys</code> resource.

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
INSERT INTO google.baremetalsolution.ssh_keys (
locationsId,
projectsId,
publicKey
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ publicKey }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: publicKey
      value: '{{ publicKey }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ssh_keys</code> resource.

```sql
/*+ delete */
DELETE FROM google.baremetalsolution.ssh_keys
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sshKeysId = '{{ sshKeysId }}';
```
