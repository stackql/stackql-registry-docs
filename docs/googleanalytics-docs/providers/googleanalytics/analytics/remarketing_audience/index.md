---
title: remarketing_audience
hide_title: false
hide_table_of_contents: false
keywords:
  - remarketing_audience
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>remarketing_audience</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.remarketing_audience</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Remarketing Audience ID. |
| `name` | `string` | The name of this remarketing audience. |
| `description` | `string` | The description of this remarketing audience. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this remarketing audience belongs. |
| `linkedViews` | `array` | The views (profiles) that this remarketing audience is linked to. |
| `audienceDefinition` | `object` | The simple audience definition that will cause a user to be added to an audience. |
| `audienceType` | `string` | The type of audience, either SIMPLE or STATE_BASED. |
| `updated` | `string` | Time this remarketing audience was last modified. |
| `created` | `string` | Time this remarketing audience was created. |
| `stateBasedAudienceDefinition` | `object` | A state based audience definition that will cause a user to be added or removed from an audience. |
| `webPropertyId` | `string` | Web property ID of the form UA-XXXXX-YY to which this remarketing audience belongs. |
| `accountId` | `string` | Account ID to which this remarketing audience belongs. |
| `kind` | `string` | Collection type. |
| `linkedAdAccounts` | `array` | The linked ad accounts associated with this remarketing audience. A remarketing audience can have only one linkedAdAccount currently. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_remarketingAudience_get` | `SELECT` | `accountId, remarketingAudienceId, webPropertyId` | Gets a remarketing audience to which the user has access. |
| `management_remarketingAudience_list` | `SELECT` | `accountId, webPropertyId` | Lists remarketing audiences to which the user has access. |
| `management_remarketingAudience_delete` | `DELETE` | `accountId, remarketingAudienceId, webPropertyId` | Delete a remarketing audience. |
| `management_remarketingAudience_insert` | `EXEC` | `accountId, webPropertyId` | Creates a new remarketing audience. |
| `management_remarketingAudience_patch` | `EXEC` | `accountId, remarketingAudienceId, webPropertyId` | Updates an existing remarketing audience. This method supports patch semantics. |
| `management_remarketingAudience_update` | `EXEC` | `accountId, remarketingAudienceId, webPropertyId` | Updates an existing remarketing audience. |
