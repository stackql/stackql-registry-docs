---
title: flink_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - flink_artifacts
  - flink_artifacts
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>flink_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flink_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.flink_artifacts.flink_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | Description of the Flink Artifact. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="class" /> | `string` | Java class or alias for the artifact as provided by developer. |
| <CopyableCode code="cloud" /> | `string` | Cloud provider where the Flink Artifact archive is uploaded. |
| <CopyableCode code="content_format" /> | `string` | Archive format of the Flink Artifact. |
| <CopyableCode code="display_name" /> | `string` | Display name of the Flink Artifact. |
| <CopyableCode code="documentation_link" /> | `string` | Document link of the Flink Artifact. |
| <CopyableCode code="environment" /> | `string` | Environment the Flink Artifact belongs to. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="region" /> | `string` | The Cloud provider region the Flink Artifact archive is uploaded. |
| <CopyableCode code="runtime_language" /> | `string` | Runtime language of the Flink Artifact. |
| <CopyableCode code="versions" /> | `array` | Versions associated with this Flink Artifact. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_artifact_v1flink_artifact" /> | `SELECT` | <CopyableCode code="cloud, id, region" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Make a request to read a flink artifact. |
| <CopyableCode code="list_artifact_v1flink_artifacts" /> | `SELECT` | <CopyableCode code="cloud, region" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Retrieve a sorted, filtered, paginated list of all flink artifacts. If no `environment` filter is specified, returns Artifacts across envs for cloud & region. |
| <CopyableCode code="create_artifact_v1flink_artifact" /> | `INSERT` | <CopyableCode code="cloud, region, data__class, data__cloud, data__display_name, data__environment, data__region, data__upload_source" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Make a request to create a flink artifact. |
| <CopyableCode code="delete_artifact_v1flink_artifact" /> | `DELETE` | <CopyableCode code="cloud, id, region" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Make a request to delete a flink artifact. |
| <CopyableCode code="update_artifact_v1flink_artifact" /> | `UPDATE` | <CopyableCode code="cloud, id, region" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Make a request to update a flink artifact. |

## `SELECT` examples

[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Flink Artifact API EA](https://img.shields.io/badge/-Request%20Access%20To%20Flink%20Artifact%20API%20EA-%23bc8540)](mailto:ccloud-api-access+artifact-v1-early-access@confluent.io?subject=Request%20to%20join%20artifact/v1%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20artifact/v1%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.) Retrieve a sorted, filtered, paginated list of all flink artifacts. If no `environment` filter is specified, returns Artifacts across envs for cloud & region.


```sql
SELECT
id,
description,
api_version,
class,
cloud,
content_format,
display_name,
documentation_link,
environment,
kind,
metadata,
region,
runtime_language,
versions
FROM confluent.flink_artifacts.flink_artifacts
WHERE cloud = '{{ cloud }}'
AND region = '{{ region }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flink_artifacts</code> resource.

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
INSERT INTO confluent.flink_artifacts.flink_artifacts (
data__cloud,
data__region,
data__environment,
data__display_name,
data__class,
data__upload_source,
cloud,
region
)
SELECT 
'{{ cloud }}',
'{{ region }}',
'{{ environment }}',
'{{ display_name }}',
'{{ class }}',
'{{ upload_source }}',
'{{ data__class }}',
'{{ data__cloud }}',
'{{ data__display_name }}',
'{{ data__environment }}',
'{{ data__region }}',
'{{ data__upload_source }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: flink_artifacts
  props:
    - name: cloud
      value: string
    - name: region
      value: string
    - name: data__class
      value: string
    - name: data__cloud
      value: string
    - name: data__display_name
      value: string
    - name: data__environment
      value: string
    - name: data__region
      value: string
    - name: data__upload_source
      value: string
    - name: cloud
      value: string
    - name: region
      value: string
    - name: environment
      value: string
    - name: display_name
      value: string
    - name: class
      value: string
    - name: content_format
      value: string
    - name: description
      value: string
    - name: documentation_link
      value: string
    - name: runtime_language
      value: string
    - name: upload_source
      props:
        - name: location
          value: string
        - name: upload_id
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>flink_artifacts</code> resource.

```sql
/*+ update */
UPDATE confluent.flink_artifacts.flink_artifacts
SET 

WHERE 
cloud = '{{ cloud }}'
AND id = '{{ id }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified <code>flink_artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.flink_artifacts.flink_artifacts
WHERE cloud = '{{ cloud }}'
AND id = '{{ id }}'
AND region = '{{ region }}';
```
