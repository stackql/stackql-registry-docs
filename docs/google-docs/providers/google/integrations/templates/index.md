---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - integrations
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

Creates, updates, deletes, gets or lists a <code>templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the template. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the template. The length should not be more than 255 characters |
| <CopyableCode code="author" /> | `string` | Optional. Creator of the template. |
| <CopyableCode code="categories" /> | `array` | Required. Categories associated with the Template. The categories listed below will be utilized for the Template listing. |
| <CopyableCode code="components" /> | `array` | Optional. Components being used in the template. This could be used to categorize and filter. |
| <CopyableCode code="createTime" /> | `string` | Output only. Auto-generated. |
| <CopyableCode code="displayName" /> | `string` | Required. The name of the template |
| <CopyableCode code="docLink" /> | `string` | Optional. Link to template documentation. |
| <CopyableCode code="lastUsedTime" /> | `string` | Optional. Time the template was last used. |
| <CopyableCode code="sharedWith" /> | `array` | Required. Resource names with which the template is shared for example ProjectNumber/Ord id |
| <CopyableCode code="tags" /> | `array` | Required. Tags which are used to identify templates. These tags could be for business use case, connectors etc. |
| <CopyableCode code="templateBundle" /> | `object` | Define the bundle of the template. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Auto-generated |
| <CopyableCode code="usageCount" /> | `string` | Optional. Number of template usages. |
| <CopyableCode code="usageInfo" /> | `string` | Optional. Information on how to use the template. This should contain detailed information about usage of the template. |
| <CopyableCode code="visibility" /> | `string` | Required. Visibility of the template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Get a template in the specified project. |
| <CopyableCode code="projects_locations_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all templates matching the filter. |
| <CopyableCode code="projects_locations_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new template |
| <CopyableCode code="projects_locations_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Deletes a template |
| <CopyableCode code="projects_locations_templates_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Updates the template by given id. |
| <CopyableCode code="projects_locations_templates_download" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Downloads a template. Retrieves the `Template` and returns the response as a string. |
| <CopyableCode code="projects_locations_templates_import" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Import the template to an existing integration. This api would keep track of usage_count and last_used_time. PERMISSION_DENIED would be thrown if template is not accessible by client. |
| <CopyableCode code="projects_locations_templates_search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Search templates based on user query and filters. This api would query the templates and return a list of templates based on the user filter. |
| <CopyableCode code="projects_locations_templates_share" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Share a template with other clients. Only the template owner can share the templates with other projects. PERMISSION_DENIED would be thrown if the request is not from the owner. |
| <CopyableCode code="projects_locations_templates_unshare" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Unshare a template from given clients. Owner of the template can unshare template with clients. Shared client can only unshare the template from itself. PERMISSION_DENIED would be thrown if request is not from owner or for unsharing itself. |
| <CopyableCode code="projects_locations_templates_upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Uploads a template. The content can be a previously downloaded template. Performs the same function as CreateTemplate, but accepts input in a string format, which holds the complete representation of the Template content. |
| <CopyableCode code="projects_locations_templates_use" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, templatesId" /> | Use the template to create integration. This api would keep track of usage_count and last_used_time. PERMISSION_DENIED would be thrown if template is not accessible by client. |

## `SELECT` examples

Lists all templates matching the filter.

```sql
SELECT
name,
description,
author,
categories,
components,
createTime,
displayName,
docLink,
lastUsedTime,
sharedWith,
tags,
templateBundle,
updateTime,
usageCount,
usageInfo,
visibility
FROM google.integrations.templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>templates</code> resource.

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
INSERT INTO google.integrations.templates (
locationsId,
projectsId,
usageInfo,
templateBundle,
docLink,
name,
lastUsedTime,
components,
sharedWith,
author,
categories,
description,
visibility,
displayName,
tags,
usageCount
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ usageInfo }}',
'{{ templateBundle }}',
'{{ docLink }}',
'{{ name }}',
'{{ lastUsedTime }}',
'{{ components }}',
'{{ sharedWith }}',
'{{ author }}',
'{{ categories }}',
'{{ description }}',
'{{ visibility }}',
'{{ displayName }}',
'{{ tags }}',
'{{ usageCount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: usageInfo
      value: '{{ usageInfo }}'
    - name: templateBundle
      value:
        - name: subIntegrationVersionTemplates
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: integrationVersionTemplate
          value:
            - name: key
              value: '{{ key }}'
            - name: integrationVersion
              value:
                - name: integrationParametersInternal
                  value:
                    - name: parameters
                      value:
                        - name: $ref
                          value: '{{ $ref }}'
                - name: runAsServiceAccount
                  value: '{{ runAsServiceAccount }}'
                - name: userLabel
                  value: '{{ userLabel }}'
                - name: cloudLoggingDetails
                  value:
                    - name: cloudLoggingSeverity
                      value: '{{ cloudLoggingSeverity }}'
                    - name: enableCloudLogging
                      value: '{{ enableCloudLogging }}'
                - name: integrationParameters
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: integrationConfigParameters
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: teardown
                  value:
                    - name: teardownTaskConfigs
                      value:
                        - name: $ref
                          value: '{{ $ref }}'
                - name: taskConfigsInternal
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: triggerConfigsInternal
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: triggerConfigs
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: lockHolder
                  value: '{{ lockHolder }}'
                - name: createdFromTemplate
                  value: '{{ createdFromTemplate }}'
                - name: errorCatcherConfigs
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: lastModifierEmail
                  value: '{{ lastModifierEmail }}'
                - name: enableVariableMasking
                  value: '{{ enableVariableMasking }}'
                - name: taskConfigs
                  value:
                    - name: $ref
                      value: '{{ $ref }}'
                - name: origin
                  value: '{{ origin }}'
                - name: description
                  value: '{{ description }}'
                - name: databasePersistencePolicy
                  value: '{{ databasePersistencePolicy }}'
                - name: parentTemplateId
                  value: '{{ parentTemplateId }}'
                - name: snapshotNumber
                  value: '{{ snapshotNumber }}'
    - name: docLink
      value: '{{ docLink }}'
    - name: name
      value: '{{ name }}'
    - name: lastUsedTime
      value: '{{ lastUsedTime }}'
    - name: components
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: sharedWith
      value:
        - name: type
          value: '{{ type }}'
    - name: author
      value: '{{ author }}'
    - name: categories
      value:
        - name: type
          value: '{{ type }}'
        - name: enumDescriptions
          value: '{{ enumDescriptions }}'
        - name: enum
          value: '{{ enum }}'
    - name: description
      value: '{{ description }}'
    - name: visibility
      value: '{{ visibility }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: tags
      value:
        - name: type
          value: '{{ type }}'
    - name: usageCount
      value: '{{ usageCount }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>templates</code> resource.

```sql
/*+ update */
UPDATE google.integrations.templates
SET 
usageInfo = '{{ usageInfo }}',
templateBundle = '{{ templateBundle }}',
docLink = '{{ docLink }}',
name = '{{ name }}',
lastUsedTime = '{{ lastUsedTime }}',
components = '{{ components }}',
sharedWith = '{{ sharedWith }}',
author = '{{ author }}',
categories = '{{ categories }}',
description = '{{ description }}',
visibility = '{{ visibility }}',
displayName = '{{ displayName }}',
tags = '{{ tags }}',
usageCount = '{{ usageCount }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND templatesId = '{{ templatesId }}';
```

## `DELETE` example

Deletes the specified <code>templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.integrations.templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND templatesId = '{{ templatesId }}';
```
