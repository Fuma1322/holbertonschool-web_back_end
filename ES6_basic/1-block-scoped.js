export default function taskBlock(trueOrFalse) {
    let task = false;
    var task2 = true;
  
    if (trueOrFalse) {
      let task = true;
      var task2 = false;
    }
  
    return [task, task2];
  }