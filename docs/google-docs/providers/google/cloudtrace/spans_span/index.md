---
title: spans_span
hide_title: false
hide_table_of_contents: false
keywords:
  - spans_span
  - cloudtrace
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

Creates, updates, deletes, gets or lists a <code>spans_span</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spans_span</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudtrace.spans_span" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_span" /> | `INSERT` | <CopyableCode code="projectsId, spansId, tracesId" /> | Creates a new span. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>spans_span</code> resource.

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
INSERT INTO google.cloudtrace.spans_span (
projectsId,
spansId,
tracesId,
name,
spanId,
parentSpanId,
displayName,
startTime,
endTime,
attributes,
stackTrace,
timeEvents,
links,
status,
sameProcessAsParentSpan,
childSpanCount,
spanKind
)
SELECT 
'{{ projectsId }}',
'{{ spansId }}',
'{{ tracesId }}',
'{{ name }}',
'{{ spanId }}',
'{{ parentSpanId }}',
'{{ displayName }}',
'{{ startTime }}',
'{{ endTime }}',
'{{ attributes }}',
'{{ stackTrace }}',
'{{ timeEvents }}',
'{{ links }}',
'{{ status }}',
true|false,
'{{ childSpanCount }}',
'{{ spanKind }}'
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
      - name: spanId
        value: '{{ spanId }}'
      - name: parentSpanId
        value: '{{ parentSpanId }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: endTime
        value: '{{ endTime }}'
      - name: attributes
        value: '{{ attributes }}'
      - name: stackTrace
        value: '{{ stackTrace }}'
      - name: timeEvents
        value: '{{ timeEvents }}'
      - name: links
        value: '{{ links }}'
      - name: status
        value: '{{ status }}'
      - name: sameProcessAsParentSpan
        value: '{{ sameProcessAsParentSpan }}'
      - name: childSpanCount
        value: '{{ childSpanCount }}'
      - name: spanKind
        value: '{{ spanKind }}'

```
</TabItem>
</Tabs>
