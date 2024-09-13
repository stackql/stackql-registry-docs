
---
title: keystores
hide_title: false
hide_table_of_contents: false
keywords:
  - keystores
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>keystore</code> resource or lists <code>keystores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keystores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keystores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Resource ID for this keystore. Values must match the regular expression `[\w[:space:].-]{1,255}`. |
| <CopyableCode code="aliases" /> | `array` | Output only. Aliases in this keystore. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_keystores_get" /> | `SELECT` | <CopyableCode code="environmentsId, keystoresId, organizationsId" /> | Gets a keystore or truststore. |
| <CopyableCode code="organizations_environments_keystores_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a keystore or truststore. - Keystore: Contains certificates and their associated keys. - Truststore: Contains trusted certificates used to validate a server's certificate. These certificates are typically self-signed certificates or certificates that are not signed by a trusted CA. |
| <CopyableCode code="organizations_environments_keystores_delete" /> | `DELETE` | <CopyableCode code="environmentsId, keystoresId, organizationsId" /> | Deletes a keystore or truststore. |

## `SELECT` examples

Gets a keystore or truststore.

```sql
SELECT
name,
aliases
FROM google.apigee.keystores
WHERE environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keystores</code> resource.

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
INSERT INTO google.apigee.keystores (
environmentsId,
organizationsId,
name,
aliases
)
SELECT 
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ name }}',
'{{ aliases }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: aliases
        value: '{{ aliases }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified keystore resource.

```sql
DELETE FROM google.apigee.keystores
WHERE environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}';
```
