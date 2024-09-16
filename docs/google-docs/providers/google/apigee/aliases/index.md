---
title: aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - aliases
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

Creates, updates, deletes, gets or lists a <code>aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.aliases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alias" /> | `string` | Resource ID for this alias. Values must match the regular expression `[^/]{1,255}`. |
| <CopyableCode code="certsInfo" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Type of alias. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_keystores_aliases_get" /> | `SELECT` | <CopyableCode code="aliasesId, environmentsId, keystoresId, organizationsId" /> | Gets an alias. |
| <CopyableCode code="organizations_environments_keystores_aliases_create" /> | `INSERT` | <CopyableCode code="environmentsId, keystoresId, organizationsId" /> | Creates an alias from a key/certificate pair. The structure of the request is controlled by the `format` query parameter: - `keycertfile` - Separate PEM-encoded key and certificate files are uploaded. Set `Content-Type: multipart/form-data` and include the `keyFile`, `certFile`, and `password` (if keys are encrypted) fields in the request body. If uploading to a truststore, omit `keyFile`. - `pkcs12` - A PKCS12 file is uploaded. Set `Content-Type: multipart/form-data`, provide the file in the `file` field, and include the `password` field if the file is encrypted in the request body. - `selfsignedcert` - A new private key and certificate are generated. Set `Content-Type: application/json` and include CertificateGenerationSpec in the request body. |
| <CopyableCode code="organizations_environments_keystores_aliases_delete" /> | `DELETE` | <CopyableCode code="aliasesId, environmentsId, keystoresId, organizationsId" /> | Deletes an alias. |
| <CopyableCode code="organizations_environments_keystores_aliases_update" /> | `REPLACE` | <CopyableCode code="aliasesId, environmentsId, keystoresId, organizationsId" /> | Updates the certificate in an alias. |
| <CopyableCode code="organizations_environments_keystores_aliases_csr" /> | `EXEC` | <CopyableCode code="aliasesId, environmentsId, keystoresId, organizationsId" /> | Generates a PKCS #10 Certificate Signing Request for the private key in an alias. |

## `SELECT` examples

Gets an alias.

```sql
SELECT
alias,
certsInfo,
type
FROM google.apigee.aliases
WHERE aliasesId = '{{ aliasesId }}'
AND environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>aliases</code> resource.

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
INSERT INTO google.apigee.aliases (
environmentsId,
keystoresId,
organizationsId,
contentType,
extensions,
data
)
SELECT 
'{{ environmentsId }}',
'{{ keystoresId }}',
'{{ organizationsId }}',
'{{ contentType }}',
'{{ extensions }}',
'{{ data }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: contentType
      value: '{{ contentType }}'
    - name: extensions
      value:
        - name: additionalProperties
          value: '{{ additionalProperties }}'
        - name: type
          value: '{{ type }}'
    - name: data
      value: '{{ data }}'

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>aliases</code> resource.

```sql
/*+ update */
REPLACE google.apigee.aliases
SET 
contentType = '{{ contentType }}',
extensions = '{{ extensions }}',
data = '{{ data }}'
WHERE 
aliasesId = '{{ aliasesId }}'
AND environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `DELETE` example

Deletes the specified <code>aliases</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.aliases
WHERE aliasesId = '{{ aliasesId }}'
AND environmentsId = '{{ environmentsId }}'
AND keystoresId = '{{ keystoresId }}'
AND organizationsId = '{{ organizationsId }}';
```
