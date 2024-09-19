---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>analyses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis} |
| <CopyableCode code="analysisResult" /> | `object` | The result of an analysis. |
| <CopyableCode code="annotatorSelector" /> | `object` | Selector of all available annotators and phrase matchers to run. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the analysis was created, which occurs when the long-running operation completes. |
| <CopyableCode code="requestTime" /> | `string` | Output only. The time at which the analysis was requested. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Gets an analysis. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Lists analyses. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Creates an analysis. The long running operation is done when the analysis has completed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Deletes an analysis. |

## `SELECT` examples

Lists analyses.

```sql
SELECT
name,
analysisResult,
annotatorSelector,
createTime,
requestTime
FROM google.contactcenterinsights.analyses
WHERE conversationsId = '{{ conversationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>analyses</code> resource.

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
INSERT INTO google.contactcenterinsights.analyses (
conversationsId,
locationsId,
projectsId,
name,
annotatorSelector
)
SELECT 
'{{ conversationsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ annotatorSelector }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: analysisResult
      value:
        - name: endTime
          value: string
        - name: callAnalysisMetadata
          value:
            - name: sentiments
              value:
                - - name: channelTag
                    value: integer
                  - name: sentimentData
                    value:
                      - name: score
                        value: number
                      - name: magnitude
                        value: number
            - name: silence
              value:
                - name: silenceDuration
                  value: string
                - name: silencePercentage
                  value: number
            - name: intents
              value: object
            - name: entities
              value: object
            - name: issueModelResult
              value:
                - name: issues
                  value:
                    - - name: score
                        value: number
                      - name: displayName
                        value: string
                      - name: issue
                        value: string
                - name: issueModel
                  value: string
            - name: phraseMatchers
              value: object
            - name: annotations
              value:
                - - name: silenceData
                    value: []
                  - name: entityMentionData
                    value:
                      - name: entityUniqueId
                        value: string
                      - name: type
                        value: string
                  - name: channelTag
                    value: integer
                  - name: interruptionData
                    value: []
                  - name: phraseMatchData
                    value:
                      - name: phraseMatcher
                        value: string
                      - name: displayName
                        value: string
                  - name: annotationEndBoundary
                    value:
                      - name: wordIndex
                        value: integer
                      - name: transcriptIndex
                        value: integer
                  - name: issueMatchData
                    value:
                      - name: issueAssignment
                        value:
                          - name: score
                            value: number
                          - name: displayName
                            value: string
                          - name: issue
                            value: string
                  - name: holdData
                    value: []
                  - name: intentMatchData
                    value:
                      - name: intentUniqueId
                        value: string
    - name: name
      value: string
    - name: createTime
      value: string
    - name: requestTime
      value: string
    - name: annotatorSelector
      value:
        - name: runSummarizationAnnotator
          value: boolean
        - name: runSentimentAnnotator
          value: boolean
        - name: issueModels
          value:
            - string
        - name: runIntentAnnotator
          value: boolean
        - name: runEntityAnnotator
          value: boolean
        - name: runPhraseMatcherAnnotator
          value: boolean
        - name: runInterruptionAnnotator
          value: boolean
        - name: runSilenceAnnotator
          value: boolean
        - name: runIssueModelAnnotator
          value: boolean
        - name: summarizationConfig
          value:
            - name: summarizationModel
              value: string
            - name: conversationProfile
              value: string
        - name: phraseMatchers
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>analyses</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.analyses
WHERE analysesId = '{{ analysesId }}'
AND conversationsId = '{{ conversationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
