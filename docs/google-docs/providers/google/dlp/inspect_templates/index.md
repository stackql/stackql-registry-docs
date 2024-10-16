---
title: inspect_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - inspect_templates
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

Creates, updates, deletes, gets or lists a <code>inspect_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inspect_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.inspect_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`; |
| <CopyableCode code="description" /> | `string` | Short description (max 256 chars). |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of an inspectTemplate. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 256 chars). |
| <CopyableCode code="inspectConfig" /> | `object` | Configuration description of the scanning process. When used with redactContent only info_types and min_likelihood are currently used. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of an inspectTemplate. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_get" /> | `SELECT` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Gets an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_delete" /> | `DELETE` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Deletes an InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_inspect_templates_patch" /> | `UPDATE` | <CopyableCode code="inspectTemplatesId, organizationsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="organizations_locations_inspect_templates_patch" /> | `UPDATE` | <CopyableCode code="inspectTemplatesId, locationsId, organizationsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_inspect_templates_patch" /> | `UPDATE` | <CopyableCode code="inspectTemplatesId, projectsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |
| <CopyableCode code="projects_locations_inspect_templates_patch" /> | `UPDATE` | <CopyableCode code="inspectTemplatesId, locationsId, projectsId" /> | Updates the InspectTemplate. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more. |

## `SELECT` examples

Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more.

```sql
SELECT
name,
description,
createTime,
displayName,
inspectConfig,
updateTime
FROM google.dlp.inspect_templates
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inspect_templates</code> resource.

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
INSERT INTO google.dlp.inspect_templates (
projectsId,
inspectTemplate,
templateId,
locationId
)
SELECT 
'{{ projectsId }}',
'{{ inspectTemplate }}',
'{{ templateId }}',
'{{ locationId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: inspectTemplate
      value:
        - name: updateTime
          value: string
        - name: inspectConfig
          value:
            - name: contentOptions
              value:
                - string
            - name: infoTypes
              value:
                - - name: sensitivityScore
                    value:
                      - name: score
                        value: string
                  - name: version
                    value: string
                  - name: name
                    value: string
            - name: minLikelihood
              value: string
            - name: includeQuote
              value: boolean
            - name: minLikelihoodPerInfoType
              value:
                - - name: minLikelihood
                    value: string
                  - name: infoType
                    value:
                      - name: version
                        value: string
                      - name: name
                        value: string
            - name: limits
              value:
                - name: maxFindingsPerRequest
                  value: integer
                - name: maxFindingsPerItem
                  value: integer
                - name: maxFindingsPerInfoType
                  value:
                    - - name: maxFindings
                        value: integer
            - name: customInfoTypes
              value:
                - - name: exclusionType
                    value: string
                  - name: storedType
                    value:
                      - name: createTime
                        value: string
                      - name: name
                        value: string
                  - name: surrogateType
                    value: []
                  - name: regex
                    value:
                      - name: groupIndexes
                        value:
                          - integer
                      - name: pattern
                        value: string
                  - name: detectionRules
                    value:
                      - - name: hotwordRule
                          value:
                            - name: proximity
                              value:
                                - name: windowBefore
                                  value: integer
                                - name: windowAfter
                                  value: integer
                            - name: likelihoodAdjustment
                              value:
                                - name: relativeLikelihood
                                  value: integer
                                - name: fixedLikelihood
                                  value: string
                  - name: dictionary
                    value:
                      - name: wordList
                        value:
                          - name: words
                            value:
                              - string
                      - name: cloudStoragePath
                        value:
                          - name: path
                            value: string
                  - name: likelihood
                    value: string
            - name: excludeInfoTypes
              value: boolean
            - name: ruleSet
              value:
                - - name: rules
                    value:
                      - - name: exclusionRule
                          value:
                            - name: matchingType
                              value: string
                            - name: excludeInfoTypes
                              value:
                                - name: infoTypes
                                  value:
                                    - - name: version
                                        value: string
                                      - name: name
                                        value: string
                            - name: excludeByHotword
                              value: []
                  - name: infoTypes
                    value:
                      - - name: version
                          value: string
                        - name: name
                          value: string
        - name: displayName
          value: string
        - name: name
          value: string
        - name: description
          value: string
        - name: createTime
          value: string
    - name: templateId
      value: string
    - name: locationId
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>inspect_templates</code> resource.

```sql
/*+ update */
UPDATE google.dlp.inspect_templates
SET 
updateMask = '{{ updateMask }}',
inspectTemplate = '{{ inspectTemplate }}'
WHERE 
inspectTemplatesId = '{{ inspectTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>inspect_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.inspect_templates
WHERE inspectTemplatesId = '{{ inspectTemplatesId }}'
AND projectsId = '{{ projectsId }}';
```
