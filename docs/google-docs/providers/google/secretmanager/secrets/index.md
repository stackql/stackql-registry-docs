
---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes or gets an <code>secret</code> resource or lists <code>secrets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.secretmanager.secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the Secret in the format `projects/*/secrets/*`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Custom metadata about the secret. Annotations are distinct from various forms of labels. Annotations exist to allow client tools to store their own state information without requiring a database. Annotation keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, begin and end with an alphanumeric character ([a-z0-9A-Z]), and may have dashes (-), underscores (_), dots (.), and alphanumerics in between these symbols. The total size of annotation keys and values must be less than 16KiB. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the Secret was created. |
| <CopyableCode code="customerManagedEncryption" /> | `object` | Configuration for encrypting secret payloads using customer-managed encryption keys (CMEK). |
| <CopyableCode code="etag" /> | `string` | Optional. Etag of the currently stored Secret. |
| <CopyableCode code="expireTime" /> | `string` | Optional. Timestamp in UTC when the Secret is scheduled to expire. This is always provided on output, regardless of what was sent on input. |
| <CopyableCode code="labels" /> | `object` | The labels assigned to this Secret. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `\p{Ll}\p{Lo}{0,62}` Label values must be between 0 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}` No more than 64 labels can be assigned to a given resource. |
| <CopyableCode code="replication" /> | `object` | A policy that defines the replication and encryption configuration of data. |
| <CopyableCode code="rotation" /> | `object` | The rotation time and period for a Secret. At next_rotation_time, Secret Manager will send a Pub/Sub notification to the topics configured on the Secret. Secret.topics must be set to configure rotation. |
| <CopyableCode code="topics" /> | `array` | Optional. A list of up to 10 Pub/Sub topics to which messages are published when control plane operations are called on the secret or its versions. |
| <CopyableCode code="ttl" /> | `string` | Input only. The TTL for the Secret. |
| <CopyableCode code="versionAliases" /> | `object` | Optional. Mapping from version alias to version name. A version alias is a string with a maximum length of 63 characters and can contain uppercase and lowercase letters, numerals, and the hyphen (`-`) and underscore ('_') characters. An alias string must start with a letter and cannot be the string 'latest' or 'NEW'. No more than 50 aliases can be assigned to a given secret. Version-Alias pairs will be viewable via GetSecret and modifiable via UpdateSecret. Access by alias is only be supported on GetSecretVersion and AccessSecretVersion. |
| <CopyableCode code="versionDestroyTtl" /> | `string` | Optional. Secret Version TTL after destruction request This is a part of the Delayed secret version destroy feature. For secret with TTL>0, version destruction doesn't happen immediately on calling destroy instead the version goes to a disabled state and destruction happens after the TTL expires. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectsId, secretsId" /> | Gets metadata for a given Secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists Secrets. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new Secret containing no SecretVersions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectsId, secretsId" /> | Deletes a Secret. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="projectsId, secretsId" /> | Updates metadata of an existing Secret. |

## `SELECT` examples

Lists Secrets.

```sql
SELECT
name,
annotations,
createTime,
customerManagedEncryption,
etag,
expireTime,
labels,
replication,
rotation,
topics,
ttl,
versionAliases,
versionDestroyTtl
FROM google.secretmanager.secrets
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets</code> resource.

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
INSERT INTO google.secretmanager.secrets (
projectsId,
name,
replication,
createTime,
labels,
topics,
expireTime,
ttl,
etag,
rotation,
versionAliases,
annotations,
versionDestroyTtl,
customerManagedEncryption
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ replication }}',
'{{ createTime }}',
'{{ labels }}',
'{{ topics }}',
'{{ expireTime }}',
'{{ ttl }}',
'{{ etag }}',
'{{ rotation }}',
'{{ versionAliases }}',
'{{ annotations }}',
'{{ versionDestroyTtl }}',
'{{ customerManagedEncryption }}'
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
      - name: replication
        value: '{{ replication }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: topics
        value: '{{ topics }}'
      - name: expireTime
        value: '{{ expireTime }}'
      - name: ttl
        value: '{{ ttl }}'
      - name: etag
        value: '{{ etag }}'
      - name: rotation
        value: '{{ rotation }}'
      - name: versionAliases
        value: '{{ versionAliases }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: versionDestroyTtl
        value: '{{ versionDestroyTtl }}'
      - name: customerManagedEncryption
        value: '{{ customerManagedEncryption }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a secret only if the necessary resources are available.

```sql
UPDATE google.secretmanager.secrets
SET 
name = '{{ name }}',
replication = '{{ replication }}',
createTime = '{{ createTime }}',
labels = '{{ labels }}',
topics = '{{ topics }}',
expireTime = '{{ expireTime }}',
ttl = '{{ ttl }}',
etag = '{{ etag }}',
rotation = '{{ rotation }}',
versionAliases = '{{ versionAliases }}',
annotations = '{{ annotations }}',
versionDestroyTtl = '{{ versionDestroyTtl }}',
customerManagedEncryption = '{{ customerManagedEncryption }}'
WHERE 
projectsId = '{{ projectsId }}'
AND secretsId = '{{ secretsId }}';
```

## `DELETE` example

Deletes the specified secret resource.

```sql
DELETE FROM google.secretmanager.secrets
WHERE projectsId = '{{ projectsId }}'
AND secretsId = '{{ secretsId }}';
```
