
---
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
  - dialogflow
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

Creates, updates, deletes or gets an <code>security_setting</code> resource or lists <code>security_settings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.security_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: `projects//locations//securitySettings/`. |
| <CopyableCode code="audioExportSettings" /> | `object` | Settings for exporting audio. |
| <CopyableCode code="deidentifyTemplate" /> | `string` | [DLP](https://cloud.google.com/dlp/docs) deidentify template name. Use this template to define de-identification configuration for the content. The `DLP De-identify Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, Dialogflow replaces sensitive info with `[redacted]` text. The template name will have one of the following formats: `projects//locations//deidentifyTemplates/` OR `organizations//locations//deidentifyTemplates/` Note: `deidentify_template` must be located in the same region as the `SecuritySettings`. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the security settings, unique within the location. |
| <CopyableCode code="insightsExportSettings" /> | `object` | Settings for exporting conversations to [Insights](https://cloud.google.com/contact-center/insights/docs). |
| <CopyableCode code="inspectTemplate" /> | `string` | [DLP](https://cloud.google.com/dlp/docs) inspect template name. Use this template to define inspect base settings. The `DLP Inspect Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, we use the default DLP inspect config. The template name will have one of the following formats: `projects//locations//inspectTemplates/` OR `organizations//locations//inspectTemplates/` Note: `inspect_template` must be located in the same region as the `SecuritySettings`. |
| <CopyableCode code="purgeDataTypes" /> | `array` | List of types of data to remove when retention settings triggers purge. |
| <CopyableCode code="redactionScope" /> | `string` | Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging. |
| <CopyableCode code="redactionStrategy" /> | `string` | Strategy that defines how we do redaction. |
| <CopyableCode code="retentionStrategy" /> | `string` | Specifies the retention behavior defined by SecuritySettings.RetentionStrategy. |
| <CopyableCode code="retentionWindowDays" /> | `integer` | Retains the data for the specified number of days. User must set a value lower than Dialogflow's default 365d TTL (30 days for Agent Assist traffic), higher value will be ignored and use default. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use default TTL. When data retention configuration is changed, it only applies to the data created after the change; the TTL of existing data created before the change stays intact. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_security_settings_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, securitySettingsId" /> | Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute. |
| <CopyableCode code="projects_locations_security_settings_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of all security settings in the specified location. |
| <CopyableCode code="projects_locations_security_settings_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create security settings in the specified location. |
| <CopyableCode code="projects_locations_security_settings_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, securitySettingsId" /> | Deletes the specified SecuritySettings. |
| <CopyableCode code="projects_locations_security_settings_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, securitySettingsId" /> | Updates the specified SecuritySettings. |

## `SELECT` examples

Returns the list of all security settings in the specified location.

```sql
SELECT
name,
audioExportSettings,
deidentifyTemplate,
displayName,
insightsExportSettings,
inspectTemplate,
purgeDataTypes,
redactionScope,
redactionStrategy,
retentionStrategy,
retentionWindowDays
FROM google.dialogflow.security_settings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_settings</code> resource.

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
INSERT INTO google.dialogflow.security_settings (
locationsId,
projectsId,
name,
displayName,
redactionStrategy,
redactionScope,
inspectTemplate,
deidentifyTemplate,
retentionWindowDays,
retentionStrategy,
purgeDataTypes,
audioExportSettings,
insightsExportSettings
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ redactionStrategy }}',
'{{ redactionScope }}',
'{{ inspectTemplate }}',
'{{ deidentifyTemplate }}',
'{{ retentionWindowDays }}',
'{{ retentionStrategy }}',
'{{ purgeDataTypes }}',
'{{ audioExportSettings }}',
'{{ insightsExportSettings }}'
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
      - name: displayName
        value: '{{ displayName }}'
      - name: redactionStrategy
        value: '{{ redactionStrategy }}'
      - name: redactionScope
        value: '{{ redactionScope }}'
      - name: inspectTemplate
        value: '{{ inspectTemplate }}'
      - name: deidentifyTemplate
        value: '{{ deidentifyTemplate }}'
      - name: retentionWindowDays
        value: '{{ retentionWindowDays }}'
      - name: retentionStrategy
        value: '{{ retentionStrategy }}'
      - name: purgeDataTypes
        value: '{{ purgeDataTypes }}'
      - name: audioExportSettings
        value: '{{ audioExportSettings }}'
      - name: insightsExportSettings
        value: '{{ insightsExportSettings }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a security_setting only if the necessary resources are available.

```sql
UPDATE google.dialogflow.security_settings
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
redactionStrategy = '{{ redactionStrategy }}',
redactionScope = '{{ redactionScope }}',
inspectTemplate = '{{ inspectTemplate }}',
deidentifyTemplate = '{{ deidentifyTemplate }}',
retentionWindowDays = '{{ retentionWindowDays }}',
retentionStrategy = '{{ retentionStrategy }}',
purgeDataTypes = '{{ purgeDataTypes }}',
audioExportSettings = '{{ audioExportSettings }}',
insightsExportSettings = '{{ insightsExportSettings }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND securitySettingsId = '{{ securitySettingsId }}';
```

## `DELETE` example

Deletes the specified security_setting resource.

```sql
DELETE FROM google.dialogflow.security_settings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND securitySettingsId = '{{ securitySettingsId }}';
```
