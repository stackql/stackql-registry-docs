---
title: goals
hide_title: false
hide_table_of_contents: false
keywords:
  - goals
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
<tr><td><b>Name</b></td><td><code>goals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.goals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Goal ID. |
| `name` | `string` | Goal name. |
| `type` | `string` | Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE, VISIT_NUM_PAGES, AND EVENT. |
| `accountId` | `string` | Account ID to which this goal belongs. |
| `internalWebPropertyId` | `string` | Internal ID for the web property to which this goal belongs. |
| `value` | `number` | Goal value. |
| `updated` | `string` | Time this goal was last modified. |
| `eventDetails` | `object` | Details for the goal of the type EVENT. |
| `selfLink` | `string` | Link for this goal. |
| `webPropertyId` | `string` | Web property ID to which this goal belongs. The web property ID is of the form UA-XXXXX-YY. |
| `visitNumPagesDetails` | `object` | Details for the goal of the type VISIT_NUM_PAGES. |
| `parentLink` | `object` | Parent link for a goal. Points to the view (profile) to which this goal belongs. |
| `created` | `string` | Time this goal was created. |
| `active` | `boolean` | Determines whether this goal is active. |
| `visitTimeOnSiteDetails` | `object` | Details for the goal of the type VISIT_TIME_ON_SITE. |
| `profileId` | `string` | View (Profile) ID to which this goal belongs. |
| `urlDestinationDetails` | `object` | Details for the goal of the type URL_DESTINATION. |
| `kind` | `string` | Resource type for an Analytics goal. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_goals_get` | `SELECT` | `accountId, goalId, profileId, webPropertyId` | Gets a goal to which the user has access. |
| `management_goals_list` | `SELECT` | `accountId, profileId, webPropertyId` | Lists goals to which the user has access. |
| `management_goals_insert` | `EXEC` | `accountId, profileId, webPropertyId` | Create a new goal. |
| `management_goals_patch` | `EXEC` | `accountId, goalId, profileId, webPropertyId` | Updates an existing goal. This method supports patch semantics. |
| `management_goals_update` | `EXEC` | `accountId, goalId, profileId, webPropertyId` | Updates an existing goal. |
