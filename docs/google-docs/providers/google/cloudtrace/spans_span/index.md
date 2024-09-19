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
{{ sameProcessAsParentSpan }},
'{{ childSpanCount }}',
'{{ spanKind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: spanId
      value: string
    - name: parentSpanId
      value: string
    - name: displayName
      value:
        - name: value
          value: string
        - name: truncatedByteCount
          value: integer
    - name: startTime
      value: string
    - name: endTime
      value: string
    - name: attributes
      value:
        - name: attributeMap
          value: object
        - name: droppedAttributesCount
          value: integer
    - name: stackTrace
      value:
        - name: stackFrames
          value:
            - name: frame
              value:
                - - name: lineNumber
                    value: string
                  - name: columnNumber
                    value: string
                  - name: loadModule
                    value: []
            - name: droppedFramesCount
              value: integer
        - name: stackTraceHashId
          value: string
    - name: timeEvents
      value:
        - name: timeEvent
          value:
            - - name: time
                value: string
              - name: annotation
                value: []
              - name: messageEvent
                value:
                  - name: type
                    value: string
                  - name: id
                    value: string
                  - name: uncompressedSizeBytes
                    value: string
                  - name: compressedSizeBytes
                    value: string
        - name: droppedAnnotationsCount
          value: integer
        - name: droppedMessageEventsCount
          value: integer
    - name: links
      value:
        - name: link
          value:
            - - name: traceId
                value: string
              - name: spanId
                value: string
              - name: type
                value: string
        - name: droppedLinksCount
          value: integer
    - name: status
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: sameProcessAsParentSpan
      value: boolean
    - name: childSpanCount
      value: integer
    - name: spanKind
      value: string

```
</TabItem>
</Tabs>
