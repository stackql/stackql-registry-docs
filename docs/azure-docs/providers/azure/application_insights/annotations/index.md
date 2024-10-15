---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>annotations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.annotations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="AnnotationName" /> | `string` | Name of annotation |
| <CopyableCode code="Category" /> | `string` | Category of annotation, free form |
| <CopyableCode code="EventTime" /> | `string` | Time when event occurred |
| <CopyableCode code="Id" /> | `string` | Unique Id for annotation |
| <CopyableCode code="Properties" /> | `string` | Serialized JSON object for detailed properties |
| <CopyableCode code="RelatedAnnotation" /> | `string` | Related parent annotation if any |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="annotationId, resourceGroupName, resourceName, subscriptionId" /> | Get the annotation for given id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="end, resourceGroupName, resourceName, start, subscriptionId" /> | Gets the list of annotations for a component for given time range |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create an Annotation of an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="annotationId, resourceGroupName, resourceName, subscriptionId" /> | Delete an Annotation of an Application Insights component. |

## `SELECT` examples

Gets the list of annotations for a component for given time range


```sql
SELECT
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation
FROM azure.application_insights.annotations
WHERE end = '{{ end }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND start = '{{ start }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>annotations</code> resource.

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
INSERT INTO azure.application_insights.annotations (
resourceGroupName,
resourceName,
subscriptionId,
AnnotationName,
Category,
EventTime,
Id,
Properties,
RelatedAnnotation
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ AnnotationName }}',
'{{ Category }}',
'{{ EventTime }}',
'{{ Id }}',
'{{ Properties }}',
'{{ RelatedAnnotation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: AnnotationName
      value: string
    - name: Category
      value: string
    - name: EventTime
      value: string
    - name: Id
      value: string
    - name: Properties
      value: string
    - name: RelatedAnnotation
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>annotations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.application_insights.annotations
WHERE annotationId = '{{ annotationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
