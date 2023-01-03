---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - clouderrorreporting
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouderrorreporting.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eventTime` | `string` | Time when the event occurred as provided in the error report. If the report did not contain a timestamp, the time the error was received by the Error Reporting system is used. |
| `message` | `string` | The stack trace that was reported or logged by the service. |
| `serviceContext` | `object` | Describes a running service that sends errors. Its version changes over time and multiple versions can run in parallel. |
| `context` | `object` | A description of the context in which an error occurred. This data should be provided by the application when reporting an error, unless the error report has been generated automatically from Google App Engine logs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_events_list` | `SELECT` | `projectsId` | Lists the specified events. |
| `projects_events_report` | `EXEC` | `projectsId` | Report an individual error event and record the event to a log. This endpoint accepts **either** an OAuth token, **or** an [API key](https://support.google.com/cloud/answer/6158862) for authentication. To use an API key, append it to the URL as the value of a `key` parameter. For example: `POST https://clouderrorreporting.googleapis.com/v1beta1/{projectName}/events:report?key=123ABC456` **Note:** [Error Reporting] (https://cloud.google.com/error-reporting) is a global service built on Cloud Logging and doesn't analyze logs stored in regional log buckets or logs routed to other Google Cloud projects. For more information, see [Using Error Reporting with regionalized logs] (https://cloud.google.com/error-reporting/docs/regionalization). |
