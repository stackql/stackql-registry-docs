
---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - aiplatform
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

Creates, updates, deletes or gets an <code>annotation</code> resource or lists <code>annotations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.annotations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Annotation. |
| <CopyableCode code="annotationSource" /> | `object` | References an API call. It contains more information about long running operation and Jobs that are triggered by the API call. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Annotation was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your Annotations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Annotation(System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Annotation: * "aiplatform.googleapis.com/annotation_set_name": optional, name of the UI's annotation set this Annotation belongs to. If not set, the Annotation is not visible in the UI. * "aiplatform.googleapis.com/payload_schema": output only, its value is the payload_schema's title. |
| <CopyableCode code="payload" /> | `any` | Required. The schema of the payload can be found in payload_schema. |
| <CopyableCode code="payloadSchemaUri" /> | `string` | Required. Google Cloud Storage URI points to a YAML file describing payload. The schema is defined as an [OpenAPI 3.0.2 Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with the parent Dataset's metadata. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Annotation was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dataItemsId, datasetsId, locationsId, projectsId" /> | Lists Annotations belongs to a dataitem This RPC is only available in InternalDatasetService. It is only used for exporting conversation data to CCAI Insights. |

## `SELECT` examples

Lists Annotations belongs to a dataitem This RPC is only available in InternalDatasetService. It is only used for exporting conversation data to CCAI Insights.

```sql
SELECT
name,
annotationSource,
createTime,
etag,
labels,
payload,
payloadSchemaUri,
updateTime
FROM google.aiplatform.annotations
WHERE dataItemsId = '{{ dataItemsId }}'
AND datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
