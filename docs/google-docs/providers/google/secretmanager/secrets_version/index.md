---
title: secrets_version
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets_version
  - secretmanager
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

Creates, updates, deletes or gets an <code>secrets_version</code> resource or lists <code>secrets_version</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.secretmanager.secrets_version" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_version" /> | `INSERT` | <CopyableCode code="projectsId, secretsId" /> | Creates a new SecretVersion containing secret data and attaches it to an existing Secret. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets_version</code> resource.

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
INSERT INTO google.secretmanager.secrets_version (
projectsId,
secretsId,
payload
)
SELECT 
'{{ projectsId }}',
'{{ secretsId }}',
'{{ payload }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: payload
        value: '{{ payload }}'

```
</TabItem>
</Tabs>
