---
title: deidentify_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - deidentify_templates
  - dlp
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

Creates, updates, deletes, gets or lists a <code>deidentify_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deidentify_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.deidentify_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID` |
| <CopyableCode code="description" /> | `string` | Short description (max 256 chars). |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of an inspectTemplate. |
| <CopyableCode code="deidentifyConfig" /> | `object` | The configuration that controls how the data will change. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 256 chars). |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of an inspectTemplate. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_get" /> | `SELECT` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Gets a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_delete" /> | `DELETE` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Deletes a DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_deidentify_templates_patch" /> | `UPDATE` | <CopyableCode code="deidentifyTemplatesId, organizationsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="organizations_locations_deidentify_templates_patch" /> | `UPDATE` | <CopyableCode code="deidentifyTemplatesId, locationsId, organizationsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_deidentify_templates_patch" /> | `UPDATE` | <CopyableCode code="deidentifyTemplatesId, projectsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |
| <CopyableCode code="projects_locations_deidentify_templates_patch" /> | `UPDATE` | <CopyableCode code="deidentifyTemplatesId, locationsId, projectsId" /> | Updates the DeidentifyTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more. |

## `SELECT` examples

Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more.

```sql
SELECT
name,
description,
createTime,
deidentifyConfig,
displayName,
updateTime
FROM google.dlp.deidentify_templates
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deidentify_templates</code> resource.

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
INSERT INTO google.dlp.deidentify_templates (
projectsId,
deidentifyTemplate,
templateId,
locationId
)
SELECT 
'{{ projectsId }}',
'{{ deidentifyTemplate }}',
'{{ templateId }}',
'{{ locationId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: deidentifyTemplate
      value:
        - name: deidentifyConfig
          value:
            - name: transformationErrorHandling
              value:
                - name: leaveUntransformed
                  value: []
                - name: throwError
                  value: []
            - name: recordTransformations
              value:
                - name: fieldTransformations
                  value:
                    - - name: infoTypeTransformations
                        value:
                          - name: transformations
                            value:
                              - - name: primitiveTransformation
                                  value:
                                    - name: fixedSizeBucketingConfig
                                      value:
                                        - name: bucketSize
                                          value: number
                                        - name: lowerBound
                                          value:
                                            - name: integerValue
                                              value: string
                                            - name: dayOfWeekValue
                                              value: string
                                            - name: floatValue
                                              value: number
                                            - name: stringValue
                                              value: string
                                            - name: timestampValue
                                              value: string
                                            - name: dateValue
                                              value:
                                                - name: day
                                                  value: integer
                                                - name: year
                                                  value: integer
                                                - name: month
                                                  value: integer
                                            - name: booleanValue
                                              value: boolean
                                            - name: timeValue
                                              value:
                                                - name: hours
                                                  value: integer
                                                - name: minutes
                                                  value: integer
                                                - name: seconds
                                                  value: integer
                                                - name: nanos
                                                  value: integer
                                    - name: dateShiftConfig
                                      value:
                                        - name: cryptoKey
                                          value:
                                            - name: transient
                                              value:
                                                - name: name
                                                  value: string
                                            - name: unwrapped
                                              value:
                                                - name: key
                                                  value: string
                                            - name: kmsWrapped
                                              value:
                                                - name: cryptoKeyName
                                                  value: string
                                                - name: wrappedKey
                                                  value: string
                                        - name: context
                                          value:
                                            - name: name
                                              value: string
                                        - name: upperBoundDays
                                          value: integer
                                        - name: lowerBoundDays
                                          value: integer
                                    - name: redactConfig
                                      value: []
                                    - name: cryptoDeterministicConfig
                                      value:
                                        - name: surrogateInfoType
                                          value:
                                            - name: sensitivityScore
                                              value:
                                                - name: score
                                                  value: string
                                            - name: version
                                              value: string
                                            - name: name
                                              value: string
                                    - name: replaceDictionaryConfig
                                      value:
                                        - name: wordList
                                          value:
                                            - name: words
                                              value:
                                                - string
                                    - name: characterMaskConfig
                                      value:
                                        - name: numberToMask
                                          value: integer
                                        - name: reverseOrder
                                          value: boolean
                                        - name: charactersToIgnore
                                          value:
                                            - - name: commonCharactersToIgnore
                                                value: string
                                              - name: charactersToSkip
                                                value: string
                                        - name: maskingCharacter
                                          value: string
                                    - name: cryptoHashConfig
                                      value: []
                                    - name: bucketingConfig
                                      value:
                                        - name: buckets
                                          value:
                                            - []
                                    - name: replaceConfig
                                      value: []
                                    - name: cryptoReplaceFfxFpeConfig
                                      value:
                                        - name: customAlphabet
                                          value: string
                                        - name: commonAlphabet
                                          value: string
                                        - name: radix
                                          value: integer
                                    - name: timePartConfig
                                      value:
                                        - name: partToExtract
                                          value: string
                                    - name: replaceWithInfoTypeConfig
                                      value: []
                                - name: infoTypes
                                  value:
                                    - - name: version
                                        value: string
                                      - name: name
                                        value: string
                      - name: condition
                        value:
                          - name: expressions
                            value:
                              - name: conditions
                                value:
                                  - name: conditions
                                    value:
                                      - - name: operator
                                          value: string
                              - name: logicalOperator
                                value: string
                      - name: fields
                        value:
                          - - name: name
                              value: string
                - name: recordSuppressions
                  value:
                    - []
            - name: imageTransformations
              value:
                - name: transforms
                  value:
                    - - name: allInfoTypes
                        value: []
                      - name: selectedInfoTypes
                        value:
                          - name: infoTypes
                            value:
                              - - name: version
                                  value: string
                                - name: name
                                  value: string
                      - name: allText
                        value: []
                      - name: redactionColor
                        value:
                          - name: blue
                            value: number
                          - name: red
                            value: number
                          - name: green
                            value: number
        - name: displayName
          value: string
        - name: description
          value: string
        - name: createTime
          value: string
        - name: updateTime
          value: string
        - name: name
          value: string
    - name: templateId
      value: string
    - name: locationId
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deidentify_templates</code> resource.

```sql
/*+ update */
UPDATE google.dlp.deidentify_templates
SET 
deidentifyTemplate = '{{ deidentifyTemplate }}',
updateMask = '{{ updateMask }}'
WHERE 
deidentifyTemplatesId = '{{ deidentifyTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>deidentify_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.deidentify_templates
WHERE deidentifyTemplatesId = '{{ deidentifyTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```
