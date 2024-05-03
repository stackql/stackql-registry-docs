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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouderrorreporting.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="context" /> | `object` | A description of the context in which an error occurred. This data should be provided by the application when reporting an error, unless the error report has been generated automatically from Google App Engine logs. |
| <CopyableCode code="eventTime" /> | `string` | Time when the event occurred as provided in the error report. If the report did not contain a timestamp, the time the error was received by the Error Reporting system is used. |
| <CopyableCode code="message" /> | `string` | The stack trace that was reported or logged by the service. |
| <CopyableCode code="serviceContext" /> | `object` | Describes a running service that sends errors. Its version changes over time and multiple versions can run in parallel. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the specified events. |
| <CopyableCode code="delete_events" /> | `DELETE` | <CopyableCode code="projectsId" /> | Deletes all error events of a given project. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists the specified events. |
| <CopyableCode code="report" /> | `EXEC` | <CopyableCode code="projectsId" /> | Report an individual error event and record the event to a log. This endpoint accepts **either** an OAuth token, **or** an [API key](https://support.google.com/cloud/answer/6158862) for authentication. To use an API key, append it to the URL as the value of a `key` parameter. For example: `POST https://clouderrorreporting.googleapis.com/v1beta1/&#123;projectName&#125;/events:report?key=123ABC456` **Note:** [Error Reporting] (https://cloud.google.com/error-reporting) is a global service built on Cloud Logging and doesn't analyze logs stored in regional log buckets or logs routed to other Google Cloud projects. |
