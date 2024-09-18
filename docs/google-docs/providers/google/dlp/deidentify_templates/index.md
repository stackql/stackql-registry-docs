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
locationId,
deidentifyTemplate,
templateId
)
SELECT 
'{{ projectsId }}',
'{{ locationId }}',
'{{ deidentifyTemplate }}',
'{{ templateId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
locationId: string
deidentifyTemplate:
  name: string
  deidentifyConfig:
    imageTransformations:
      transforms:
        - allInfoTypes: {}
          selectedInfoTypes:
            infoTypes:
              - version: string
                name: string
                sensitivityScore:
                  score: string
          redactionColor:
            blue: number
            red: number
            green: number
          allText: {}
    recordTransformations:
      fieldTransformations:
        - condition:
            expressions:
              logicalOperator: string
              conditions:
                conditions:
                  - operator: string
                    value:
                      timestampValue: string
                      dateValue:
                        month: integer
                        year: integer
                        day: integer
                      dayOfWeekValue: string
                      stringValue: string
                      booleanValue: boolean
                      timeValue:
                        nanos: integer
                        minutes: integer
                        seconds: integer
                        hours: integer
                      floatValue: number
                      integerValue: string
                    field:
                      name: string
          primitiveTransformation:
            replaceDictionaryConfig:
              wordList:
                words:
                  - type: string
            cryptoDeterministicConfig:
              cryptoKey:
                unwrapped:
                  key: string
                transient:
                  name: string
                kmsWrapped:
                  cryptoKeyName: string
                  wrappedKey: string
              surrogateInfoType:
                version: string
                name: string
            bucketingConfig:
              buckets:
                - {}
            replaceWithInfoTypeConfig: {}
            characterMaskConfig:
              numberToMask: integer
              charactersToIgnore:
                - commonCharactersToIgnore: string
                  charactersToSkip: string
              reverseOrder: boolean
              maskingCharacter: string
            timePartConfig:
              partToExtract: string
            cryptoHashConfig: {}
            redactConfig: {}
            dateShiftConfig:
              lowerBoundDays: integer
              upperBoundDays: integer
            fixedSizeBucketingConfig:
              bucketSize: number
            replaceConfig: {}
            cryptoReplaceFfxFpeConfig:
              commonAlphabet: string
              customAlphabet: string
              radix: integer
          infoTypeTransformations:
            transformations:
              - infoTypes:
                  - version: string
                    name: string
          fields:
            - name: string
      recordSuppressions:
        - {}
    transformationErrorHandling:
      leaveUntransformed: {}
      throwError: {}
  createTime: string
  description: string
  updateTime: string
  displayName: string
templateId: string

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
