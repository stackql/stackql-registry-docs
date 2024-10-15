---
title: threat_intelligence_indicators
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicators
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>threat_intelligence_indicators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>threat_intelligence_indicators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.threat_intelligence_indicators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of the threat intelligence entity |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | View a threat intelligence indicator by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get all threat intelligence indicators. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Update a threat Intelligence indicator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Delete a threat intelligence indicator. |
| <CopyableCode code="append_tags" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Append tags to a threat intelligence indicator. |
| <CopyableCode code="query_indicators" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Query threat intelligence indicators as per filtering criteria. |

## `SELECT` examples

Get all threat intelligence indicators.


```sql
SELECT
etag,
kind
FROM azure.sentinel.threat_intelligence_indicators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>threat_intelligence_indicators</code> resource.

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
INSERT INTO azure.sentinel.threat_intelligence_indicators (
name,
resourceGroupName,
subscriptionId,
workspaceName,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: []
    - name: properties
      value:
        - name: additionalData
          value: object
        - name: friendlyName
          value: string
        - name: threatIntelligenceTags
          value:
            - string
        - name: lastUpdatedTimeUtc
          value: string
        - name: source
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: indicatorTypes
          value:
            - string
        - name: pattern
          value: string
        - name: patternType
          value: string
        - name: patternVersion
          value: string
        - name: killChainPhases
          value:
            - - name: killChainName
                value: string
              - name: phaseName
                value: string
        - name: parsedPattern
          value:
            - - name: patternTypeKey
                value: string
              - name: patternTypeValues
                value:
                  - - name: valueType
                      value: string
                    - name: value
                      value: string
        - name: externalId
          value: string
        - name: createdByRef
          value: string
        - name: defanged
          value: boolean
        - name: externalLastUpdatedTimeUtc
          value: string
        - name: externalReferences
          value:
            - - name: description
                value: string
              - name: externalId
                value: string
              - name: sourceName
                value: string
              - name: url
                value: string
              - name: hashes
                value: object
        - name: granularMarkings
          value:
            - - name: language
                value: string
              - name: markingRef
                value: integer
              - name: selectors
                value:
                  - string
        - name: labels
          value:
            - string
        - name: revoked
          value: boolean
        - name: confidence
          value: integer
        - name: objectMarkingRefs
          value:
            - string
        - name: language
          value: string
        - name: threatTypes
          value:
            - string
        - name: validFrom
          value: string
        - name: validUntil
          value: string
        - name: created
          value: string
        - name: modified
          value: string
        - name: extensions
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>threat_intelligence_indicators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.threat_intelligence_indicators
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
