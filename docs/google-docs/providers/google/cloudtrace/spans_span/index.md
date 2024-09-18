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
name: string
spanId: string
parentSpanId: string
displayName:
  value: string
  truncatedByteCount: integer
startTime: string
endTime: string
attributes:
  attributeMap: object
  droppedAttributesCount: integer
stackTrace:
  stackFrames:
    frame:
      - lineNumber: string
        columnNumber: string
        loadModule: {}
    droppedFramesCount: integer
  stackTraceHashId: string
timeEvents:
  timeEvent:
    - time: string
      annotation: {}
      messageEvent:
        type: string
        id: string
        uncompressedSizeBytes: string
        compressedSizeBytes: string
  droppedAnnotationsCount: integer
  droppedMessageEventsCount: integer
links:
  link:
    - traceId: string
      spanId: string
      type: string
  droppedLinksCount: integer
status:
  code: integer
  message: string
  details:
    - type: string
      additionalProperties: any
sameProcessAsParentSpan: boolean
childSpanCount: integer
spanKind: string

```
</TabItem>
</Tabs>
