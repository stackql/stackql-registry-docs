---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - notebooks
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
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.notebooks.schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of this schedule. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}` |
| `description` | `string` | A brief description of this environment. |
| `updateTime` | `string` | Output only. Time the schedule was last updated. |
| `timeZone` | `string` | Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT). |
| `displayName` | `string` | Output only. Display name used for UI purposes. Name can only contain alphanumeric characters, hyphens '-', and underscores '_'. |
| `recentExecutions` | `array` | Output only. The most recent execution names triggered from this schedule and their corresponding states. |
| `createTime` | `string` | Output only. Time the schedule was created. |
| `cronSchedule` | `string` | Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html |
| `executionTemplate` | `object` | The description a notebook execution workload. |
| `state` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_schedules_get` | `SELECT` | `locationsId, projectsId, schedulesId` | Gets details of schedule |
| `projects_locations_schedules_list` | `SELECT` | `locationsId, projectsId` | Lists schedules in a given project and location. |
| `projects_locations_schedules_create` | `INSERT` | `locationsId, projectsId` | Creates a new Scheduled Notebook in a given project and location. |
| `projects_locations_schedules_delete` | `DELETE` | `locationsId, projectsId, schedulesId` | Deletes schedule and all underlying jobs |
| `projects_locations_schedules_trigger` | `EXEC` | `locationsId, projectsId, schedulesId` | Triggers execution of an existing schedule. |
