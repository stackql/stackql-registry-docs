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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.security_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the settings. Required for the SecuritySettingsService.UpdateSecuritySettings method. SecuritySettingsService.CreateSecuritySettings populates the name automatically. Format: `projects//locations//securitySettings/`. |
| `redactionStrategy` | `string` | Strategy that defines how we do redaction. |
| `inspectTemplate` | `string` | [DLP](https://cloud.google.com/dlp/docs) inspect template name. Use this template to define inspect base settings. The `DLP Inspect Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, we use the default DLP inspect config. The template name will have one of the following formats: `projects//locations//inspectTemplates/` OR `organizations//locations//inspectTemplates/` Note: `inspect_template` must be located in the same region as the `SecuritySettings`. |
| `retentionWindowDays` | `integer` | Retains data in interaction logging for the specified number of days. This does not apply to Cloud logging, which is owned by the user - not Dialogflow. User must set a value lower than Dialogflow's default 365d TTL. Setting a value higher than that has no effect. A missing value or setting to 0 also means we use Dialogflow's default TTL. Note: Interaction logging is a limited access feature. Talk to your Google representative to check availability for you. |
| `audioExportSettings` | `object` | Settings for exporting audio. |
| `displayName` | `string` | Required. The human-readable name of the security settings, unique within the location. |
| `insightsExportSettings` | `object` | Settings for exporting conversations to [Insights](https://cloud.google.com/contact-center/insights/docs). |
| `purgeDataTypes` | `array` | List of types of data to remove when retention settings triggers purge. |
| `deidentifyTemplate` | `string` | [DLP](https://cloud.google.com/dlp/docs) deidentify template name. Use this template to define de-identification configuration for the content. The `DLP De-identify Templates Reader` role is needed on the Dialogflow service identity service account (has the form `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com`) for your agent's project. If empty, Dialogflow replaces sensitive info with `[redacted]` text. The template name will have one of the following formats: `projects//locations//deidentifyTemplates/` OR `organizations//locations//deidentifyTemplates/` Note: `deidentify_template` must be located in the same region as the `SecuritySettings`. |
| `redactionScope` | `string` | Defines the data for which Dialogflow applies redaction. Dialogflow does not redact data that it does not have access to – for example, Cloud logging. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_securitySettings_get` | `SELECT` | `locationsId, projectsId, securitySettingsId` | Retrieves the specified SecuritySettings. The returned settings may be stale by up to 1 minute. |
| `projects_locations_securitySettings_list` | `SELECT` | `locationsId, projectsId` | Returns the list of all security settings in the specified location. |
| `projects_locations_securitySettings_create` | `INSERT` | `locationsId, projectsId` | Create security settings in the specified location. |
| `projects_locations_securitySettings_delete` | `DELETE` | `locationsId, projectsId, securitySettingsId` | Deletes the specified SecuritySettings. |
| `projects_locations_securitySettings_patch` | `EXEC` | `locationsId, projectsId, securitySettingsId` | Updates the specified SecuritySettings. |
