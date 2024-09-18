---
title: user_workloads_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - user_workloads_secrets
  - composer
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

Creates, updates, deletes, gets or lists a <code>user_workloads_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_workloads_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.user_workloads_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the Secret, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}" |
| <CopyableCode code="data" /> | `object` | Optional. The "data" field of Kubernetes Secret, organized in key-value pairs, which can contain sensitive values such as a password, a token, or a key. The values for all keys have to be base64-encoded strings. For details see: https://kubernetes.io/docs/concepts/configuration/secret/ |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Gets an existing user workloads Secret. Values of the "data" field in the response are cleared. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Creates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Deletes a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="environmentsId, locationsId, projectsId, userWorkloadsSecretsId" /> | Updates a user workloads Secret. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. |

## `SELECT` examples

Lists user workloads Secrets. This method is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer.

```sql
SELECT
name,
data
FROM google.composer.user_workloads_secrets
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_workloads_secrets</code> resource.

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
INSERT INTO google.composer.user_workloads_secrets (
environmentsId,
locationsId,
projectsId,
name,
data
)
SELECT 
'{{ environmentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ data }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
data: object

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>user_workloads_secrets</code> resource.

```sql
/*+ update */
REPLACE google.composer.user_workloads_secrets
SET 
name = '{{ name }}',
data = '{{ data }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND userWorkloadsSecretsId = '{{ userWorkloadsSecretsId }}';
```

## `DELETE` example

Deletes the specified <code>user_workloads_secrets</code> resource.

```sql
/*+ delete */
DELETE FROM google.composer.user_workloads_secrets
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND userWorkloadsSecretsId = '{{ userWorkloadsSecretsId }}';
```
